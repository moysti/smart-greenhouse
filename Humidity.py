import time
import board
import adafruit_dht

sensor = adafruit_dht.DHT11(board.D4)

fileHmd = open("hmd.txt", "a")
fileTmp = open("temp.txt", "a")

while True:
    try:
        # Print the values to the serial port
        temperature = sensor.temperature
        humidity = sensor.humidity
        #print("Temp={0:0.1f}C, Humidity={2:0.1f}%".format(temperature_c, humidity))
        
        fileTmp.write(str(temperature) + "\n")
        fileHmd.write(str(humidity) + "\n")
        
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(3.0)