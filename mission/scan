#! /usr/bin/env python3
# _*_ coding:utf-8 _*_

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import UInt8

class scan():
	def __init__(self):
		self.sub_scan_obstacle = rospy.Subscriber('/scan', LaserScan, self.scan_cb, queue_size=1)
		self.sub_angle = rospy.Subscriber('/angle', UInt8, self.angle_cb, queue_size = 1)
		self.angle = 0 

	def angle_cb(self, angle):
		angle = angle.data
		print(angle)

	def scan_cb(self, scan):
		global left_min, right_min, left_min_index, right_min_index
		
		scan = scan.ranges
		
		scan_left_tuple = scan[0:180] #[850:95]
		self.scan_left_list = list(scan_left_tuple)
		
		for i in self.scan_left_list: #except
			if i < 0.01:
				zero = self.scan_left_list.index(i)
				self.scan_left_list[zero] = 9
			else:	
				pass

		scan_right_tuple = scan[180:360] #[265:275]
		self.scan_right_list = list(scan_right_tuple)
		self.scan_right_list = self.scan_right_list[::-1]
		for i in self.scan_right_list:	
			if i < 0.01:
				zero = self.scan_right_list.index(i)
				self.scan_right_list[zero] = 9
				#print scan_right	
			else:
				pass
		
		self.left_min = min(self.scan_left_list)
		self.left_min_index = self.scan_left_list.index(self.left_min)
		
		self.right_min = min(self.scan_right_list)
		self.right_min_index = self.scan_right_list.index(self.right_min)
		
		self.scan_left_list_2 = self.scan_left_list[50:60]
		self.scan_left_list_2 = min(self.scan_left_list_2)
		
		#print(self.left_min)

	def main(self):
		rospy.spin()
#def control():
	
if __name__ == "__main__":
	rospy.init_node('scan')
	node = scan()
	node.main()
#else:
