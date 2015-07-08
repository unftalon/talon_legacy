from util import *
import serial, json
import time

class Communicator:

	def __init__(self, interface='/dev/ttyACM0', baud_rate=9600):
		self.communication = serial.Serial(interface, baud_rate, timeout=0)		

	def writePoint(self, point):
	
		send = json.dumps({"object_type": "point", "success": 0, "x":point.getX(), "y":point.getY()})
		self.communication.write(send)
		time.sleep(2)

		
	def sendSuccess(self):
	
		self.communication.write("1")
		time.sleep(1)
		
	def listen(self):
	
		thread = threading.Thread(target=self.read)
		thread.daemon = True
		thread.start()
		
	def read(self):

		while True:
			
			line = self.communication.readline()
			print line
			time.sleep(1)
			
	def	standBy(self):

		while True:
			
			time.sleep(1)
			line = self.communication.readline()
			
			if not line:
				continue
			else:
				
				task_num = int(line)
				return task_num
			
				
			
			