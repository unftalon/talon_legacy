from util import *

class PointTaskResult:
    def __init__(self, cv2, options):
        self.xValue = int(options[0])
        self.yValue = int(options[1])
        self.options = options
        self.cv2 = cv2

    def drawOnFrame(self, frame):
        self.cv2.circle(frame, (self.xValue, self.yValue), 40, (0,0,255), 5)

class RectangeCollectionTaskResult:
    def __init__(self, cv2, options):
        self.rectangles = options
        self.thickness = 5
        self.color = RED
        self.cv2 = cv2

    def drawOnFrame(self, frame):
        for rect in self.rectangles:
            self.cv2.drawContours(frame, [rect], 0, self.color, self.thickness)
