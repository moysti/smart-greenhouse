import time
import adafruit_dht
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_TOPIC = "greenhouse/temp"
MQTT_TOPIC2 = "greenhouse/humidity"

sensor = adafruit_dht.DHT11(board.D22)

client = mqtt.Client()
client.connect(MQTT_BROKER)

try:
    while True:
        try:
            temperature = sensor.temperature
            humidity = sensor.humidity
            print(f"Temp: {temperature}°C, Humidity: {humidity}%")

            # send temperature as string
            client.publish(MQTT_TOPIC, str(temperature))
            client.publish(MQTT_TOPIC2, str(humidity))

        except RuntimeError as e:
            print(f"DHT read error: {e.args[0]}")
        time.sleep(3)

except KeyboardInterrupt:
    sensor.exit()
    client.disconnect()
