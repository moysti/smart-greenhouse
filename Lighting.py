import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LDR_PIN = 6         
LED_PIN = 17        
THRESHOLD = 500000     

# Setup LED pin
GPIO.setup(LED_PIN, GPIO.OUT)

def rc_time(pin):
    reading = 0
    # Discharge the capacitor
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
    time.sleep(0.1)

    # Set pin to input to measure charging time
    GPIO.setup(pin, GPIO.IN)

    # Measure time until pin goes HIGH
    while GPIO.input(pin) == GPIO.LOW:
        reading += 1

    return reading

try:
    while True:
        light_level = rc_time(LDR_PIN)
        print(f"Light level: {light_level}") #higher = darker

        if light_level > THRESHOLD:
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
        else:
            GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED off

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
