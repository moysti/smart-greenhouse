import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

MQTT_BROKER = "localhost"
MQTT_TOPIC = "greenhouse/waterlevel"

client = mqtt.Client()
client.connect(MQTT_BROKER)

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def distanz():
    GPIO.output(GPIO_TRIGGER, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartZeit = time.time()
    StopZeit = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        if StopZeit <= (StartZeit - 2) : return None
        StartZeit = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()

    TimeElapsed = StopZeit - StartZeit
    distanz = (TimeElapsed * 34300) / 2

    return distanz



while True:
    abstand = distanz()
    if abstand is not None:
        print("Gemessene Entfernung = %.1f cm" % abstand)
        client.publish(MQTT_TOPIC, str(abstand))
    time.sleep(1)
