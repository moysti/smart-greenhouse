import time
import board
import adafruit_dht

sensor = adafruit_dht.DHT11(board.D4)

fileHmd = open("hmd.txt", "a")
fileTmp = open("temp.txt", "a")

while True:
    try:
        temperature = sensor.temperature
        humidity = sensor.humidity

        fileTmp.write(str(temperature) + "\n")
        fileHmd.write(str(humidity) + "\n")
        
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(3.0)