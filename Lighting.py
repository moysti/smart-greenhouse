import RPi.GPIO as GPIO
import time
from sense_hat import SenseHat

GPIO.setmode(GPIO.BCM)
LDR_PIN = 6 

sense = SenseHat()
THRESHOLD = 500000

def rc_time(pin):
    reading = 0
    # Discharge the capacitor
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
    time.sleep(0.1)

    # Change the pin to input to measure charge time
    GPIO.setup(pin, GPIO.IN)

    # Count until the pin goes HIGH (capacitor charged)
    while GPIO.input(pin) == GPIO.LOW:
        reading += 1

    return reading

try:
    while True:
        light_level = rc_time(LDR_PIN)
        print(f"Light level: {light_level}") # higher = darker

        if light_level > THRESHOLD:
            sense.clear((255, 255, 255))  # bright white light
        else:
            sense.clear()  # turn off LEDs

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    sense.clear()
