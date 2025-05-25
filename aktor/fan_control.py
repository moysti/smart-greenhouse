import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

FAN_PIN = 5
THRESHOLD_TEMP = 26.6  # °C

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("greenhouse/temp")

def on_message(client, userdata, msg):
    try:
        temp = float(msg.payload.decode())
        print(f"Received temperature: {temp}°C")

        if temp >= THRESHOLD_TEMP:
            print("Fan ON")
            GPIO.output(FAN_PIN, GPIO.HIGH)
        else:
            print("Fan OFF")
            GPIO.output(FAN_PIN, GPIO.LOW)
    except ValueError:
        print("Invalid temperature value")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost")
client.loop_forever()
