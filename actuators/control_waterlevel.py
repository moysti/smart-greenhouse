import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from time import sleep

LED_PIN = 27
THRESHOLD = 3
MQTT_TOPIC = "greenhouse/waterlevel"

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        value = float(msg.payload.decode())
        print(f"Received: {value}")
        if value < THRESHOLD:
            GPIO.output(LED_PIN, GPIO.HIGH)
            sleep(0.3)
            GPIO.output(LED_PIN, GPIO.LOW)
            sleep(0.1)
        else:
          GPIO.output(LED_PIN, GPIO.HIGH)
    except ValueError:
        print("Invalid payload")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.2.138") 

client.loop_forever()