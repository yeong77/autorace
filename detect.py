#!/usr/bin/env python3

import jetson.inference
import jetson.utils


# load the object detection model
net = jetson.inference.detectNet(argv=['--model=/home/yy/jetson-inference/python/training/detection/ssd/mobilenet/ssd-mobilenet.onnx', '--labels=/home/yy/jetson-inference/python/training/detection/ssd/mobilenet/labels.txt', '--input-blob=input_0', '--output-cvg=scores', '--output-bbox=boxes'])  #, '--threshold=0.8'

########################################


# set up camera
camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' or 'csi://0'

# set up display for output to screen
display = jetson.utils.videoOutput("display://0")


p

while True: #display.IsStreaming():		# while display window is open
	img = camera.Capture()		# take incoming video frame
	detections = net.Detect(img)	# detect objects in the frame and save to detection variable
	display.Render(img)		# show the frame
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))	# show FPS of camera
	for detection in detections:
		if detection.ClassID == 15:
			center_x = detection.Left + (detection.Right - detection.Left) /2
			print(center_x)
			print(detection.Center)
