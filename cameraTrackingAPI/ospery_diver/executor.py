import threading
from util import *

class Executor:

	def __init__(self, cv2, numpy):
		self.cv2 = cv2
		self.numpy = numpy   	

	def run(self,task, image, color):

		return task(self.cv2, self.numpy, image, color)


		




		

	
	