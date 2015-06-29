from util import *
import serial, json

class Communicator:

	def __init__(self, interface='/dev/ttyACM0', baud_rate=9600):
		self.communication = serial.Serial(interface, baud_rate, timeout=0)

	def writePoint(self, point):
		send = json.dumps({'object_type': 'point', 'x':str(point.getX()), 'y':str(point.getY())})
		self.communication.write('x')