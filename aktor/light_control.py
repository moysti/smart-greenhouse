import mqtt.client as mqtt
import RPi.GPIO as GPIO

LED_PIN = 17
THRESHOLD = 500000
MQTT_TOPIC = "greenhouse/light"

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        value = int(msg.payload.decode())
        print(f"Received: {value}")
        if value > THRESHOLD:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
    except ValueError:
        print("Invalid payload")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost") 

client.loop_forever()

