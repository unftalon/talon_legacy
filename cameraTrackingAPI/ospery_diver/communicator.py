from util import *
import serial, json
import time

class Communicator:

	def __init__(self, interface='/dev/ttyACM0', baud_rate=9600):
		self.communication = serial.Serial(interface, baud_rate, timeout=0)
		self.jobNumber = 0

	def writePoint(self, point):
	
		send = json.dumps({"job_number":self.jobNumber,"object_type": "point", "success": 0, "x":point.getX(), "y":point.getY()})
		self.communication.write(send)
		time.sleep(2)
		
	def listen(self):
	
		thread = threading.Thread(target=self.read)
		thread.daemon = True
		thread.start()
		
	def read(self):

		while True:
			
			line = self.communication.readline()
			print line
		
			time.sleep(1)
			