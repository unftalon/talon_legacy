from util import *
import serial, json
import time


class Communicator:
	
	def __init__(self, interface='/dev/ttyACM0', baud_rate=9600):
		self.communication = serial.Serial(interface, baud_rate, timeout=0)		
		self.DELAY = 2

	def writePoint(self, point):
	
	
		self.communication.write("0")
		time.sleep(self.DELAY)
		self.communication.write(str(point[1]))
		time.sleep(self.DELAY)
		
	def	standBy(self):

		while True:
			
			time.sleep(self.DELAY)
			line = self.communication.readline()
			
			if not line:
				continue
			else:
				
				task_num = int(line)
				return task_num
			
				
			
			