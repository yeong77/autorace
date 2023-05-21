#!/usr/bin/env python3

import jetson.inference
import jetson.utils
import rospy
from std_msgs.msg import UInt8

# load the object detection model
net = jetson.inference.detectNet(argv=['--model=/home/yy/jetson-inference/python/training/detection/ssd/mobilenet/ssd-mobilenet.onnx', '--labels=/home/yy/jetson-inference/python/training/detection/ssd/mobilenet/labels.txt', '--input-blob=input_0', '--output-cvg=scores', '--output-bbox=boxes'])  #, '--threshold=0.8'

########################################


# set up camera
camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' or 'csi://0'

# set up display for output to screen
display = jetson.utils.videoOutput("display://0")

rospy.init_node('detect')
pub_angle = rospy.Publisher('/angle', UInt8, queue_size =1)

while True: #display.IsStreaming():		# while display window is open
	img = camera.Capture()	# take incoming video frame
	detections = net.Detect(img)	# detect objects in the frame and save to detection variable
			
	for detection in detections:
		angle = UInt8()
		if detection.ClassID == 15:
			display.Render(img)		# show the frame
			display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))	# show FPS of camera
			center_x = detection.Left + (detection.Right - detection.Left) /2
			center_x = 51 + ( 78 / 1280 ) * center_x
			angle.data = center_x
			pub_angle.publish = angle.data
			print("center_x : ", center_x)
			print("height : ", detection.Height)


