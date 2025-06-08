import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

LDR_PIN = 6
MQTT_BROKER = "localhost"  
MQTT_TOPIC = "greenhouse/light"

def rc_time(pin):
    reading = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
    time.sleep(0.1)
    GPIO.setup(pin, GPIO.IN)
    while GPIO.input(pin) == GPIO.LOW:
        reading += 1
    return reading

GPIO.setmode(GPIO.BCM)
client = mqtt.Client()
client.connect(MQTT_BROKER)

try:
    while True:
        value = rc_time(LDR_PIN)
        print("Send light value:", value)
        client.publish(MQTT_TOPIC, value)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    client.disconnect()

