import time

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
from gpiozero import AngularServo

SERVO_PIN = TODO()
THRESHOLD_HUM = 40 # %

MQTT_BROKER = "localhost"
MQTT_TOPIC = "greenhouse/humidity"

s = AngularServo(SERVO_PIN, min_angle=-90, max_angle=90)

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        hum = float(msg.payload.decode())
        print(f"Received humidity: {hum}%")

        if hum <= THRESHOLD_HUM:
            print("Water Bottle go!")
            s.angle = int(90)
            time.sleep(3)
            s.angle = int(-90)
        else:
            print("Water Bottle OFF")
    except ValueError:
        print("Invalid Humidity value")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER)
client.loop_forever()
