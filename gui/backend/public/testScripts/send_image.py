import paho.mqtt.client as mqtt
import cv2
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)
cam = cv2.VideoCapture(0)

if not cam.isOpened(): 
	print("Failed to open camera")
	exit()

print("Start video stream")
try: 
	while True: 
		ret, frame = cam.read()
		frame = cv2.resize(frame, (90, 68))
		if not ret: 
			print("Failed to capture image")
			continue
		ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 60])
		if not ret:
			print("Failed to encode image.")
			continue
		jpg_bytes = buffer.tobytes()
		client.publish("video", jpg_bytes, qos=0, retain=False)
		time.sleep(1)
except KeyboardInterrupt: 
	print("Stopping...")
finally: 
	cam.release()
	client.disconnect()

