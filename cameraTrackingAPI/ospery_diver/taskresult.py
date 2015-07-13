from util import *

class TaskResult:
    def __init__(self):
        return
		
    def value(self):
        return None
		
    def arrayValue(self):
        return None
		
class PointTaskResult(TaskResult):
	def __init__(self, cv2, options):
		TaskResult.__init__(self)
		self.xValue = int(options[0])
		self.yValue = int(options[1])
		self.options = options
		self.cv2 = cv2
		
	def value(self):
		return [self.xValue, self.yValue]
		
	def drawOnFrame(self, frame):
		self.cv2.circle(frame, (self.xValue, self.yValue), 40, (0,0,255), 5)
		
class BuoyTaskResult(TaskResult):
	def __init__(self, cv2, options):
		TaskResult.__init__(self)
		self.xValue = int(options[0])
		self.yValue = int(options[1])
		self.radius = int(options[2])
		self.options = options
		self.cv2 = cv2
		
	def value(self):
		return [self.xValue, self.yValue, self.radius]
	
	def drawOnFrame(self, frame):
		self.cv2.circle(frame, (self.xValue, self.yValue), self.radius, (0,0,255), 5)

class RectangeCollectionTaskResult(TaskResult):

    def __init__(self, cv2, options):
        TaskResult.__init__(self)
        self.rectangles = options
        self.thickness = 5
        self.color = RED
        self.cv2 = cv2

    def drawOnFrame(self, frame):
        for rect in self.rectangles:
            self.cv2.drawContours(frame, [rect], 0, self.color, self.thickness)

class UnsuccessfulTaskResult(TaskResult):
    def __init__(self, foo=None):
        TaskResult.__init__(self)

    def result():
        #print "unsuccessfull"
        return UnsuccessfulResult()

    def drawOnFrame(self, frame):
        #print "unsuccessful"
        return

class UnsuccessfulResult:
    def __init__(self, foo=None):
        return
