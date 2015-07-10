import numpy as np
import cv2
import sys
import Queue
import threading


# openCV will only work with Numpy Arrays
# the three item represented in HSV (Hue, Saturation, and Value)
ORANGE = { 'lower': np.array([5, 100, 100],np.uint8),  'upper': np.array([15, 230, 255],np.uint8) };
BLUE = { 'lower': np.array([100, 125, 30],np.uint8),  'upper': np.array([170, 240, 230],np.uint8) };
GREEN = { 'lower': np.array([60, 80, 30],np.uint8),  'upper': np.array([90, 240, 215],np.uint8) };
YELLOW = { 'lower': np.array([25, 155, 100],np.uint8),  'upper': np.array([45, 240, 200],np.uint8) };
RED = (0,0,255)
INREMENT_VALUE = 5
ALLCOLORS = { 'lower': np.array([0, 00, 00],np.uint8),  'upper': np.array([255, 255, 255],np.uint8) };

def orange():
    return ORANGE

def all_colors():
    return ALLCOLORS

KMEANS_FLAG = cv2.KMEANS_RANDOM_CENTERS

KMEANS_CRITERIA = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

KMEANS_ATTEMPTS = 10

# Minimum distance between the centers of the detected circles (in pixels)
MIN_DIST = 1

MARGIN_FROM_CENTER = 150


def getCenter(points):
    ret, labels, center = cv2.kmeans(points, 1, KMEANS_CRITERIA, KMEANS_ATTEMPTS, 0)
    center = center[0]
    return Point(int(center[0]), int(center[1]))
	
def isCentered(x, y, frame, margin=MARGIN_FROM_CENTER):
	point = distFromCenter(frame ,Point(x,y))
	if abs(point.getX()) <= margin and abs(point.getY()) <= margin:
		return True
	else:
		return False

	
def findLargestAreaCircle(image, method=cv2.cv.CV_HOUGH_GRADIENT, dp=20, min_dist=MIN_DIST):
	

	
	circles = cv2.HoughCircles(image, cv2.cv.CV_HOUGH_GRADIENT, min_dist, 20, param1=40, param2=20, minRadius=30, maxRadius=0)
			  

	if circles is not None:
		
		largestCircle = Circle()
		
		for (x, y, r) in circles[0]:
		
			if int(r) > largestCircle.getRadius():
				
				largestCircle = Circle(x, y, r)
		
		return largestCircle
	
	else:
		
		return None

def parse_letter(letter):
    return {
        'a': [ 1, 'upper', 0], #HUE],
        's': [ 1, 'upper', 1], #SATURATION],
        'd': [ 1, 'upper', 2], #VALUE],
        'z': [-1, 'upper', 0], #HUE],
        'x': [-1, 'upper', 1], #SATURATION],
        'c': [-1, 'upper', 2], #VALUE],

        'f': [ 1, 'lower', 0], #HUE],
        'g': [ 1, 'lower', 1], #SATURATION],
        'h': [ 1, 'lower', 2], #VALUE],
        'v': [-1, 'lower', 0], #HUE],
        'b': [-1, 'lower', 1], #SATURATION],
        'n': [-1, 'lower', 2], #VALUE],
    }[letter]

def detectColor(image, color):
    # find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(image, color['lower'], color['upper'])

    # Do a bitwise and with the original and mask. This will provide an insection.
    # All pixels in the mask that correspond to the original will be recognized as a
    # binary 1
    output = cv2.bitwise_and(image, image, mask = mask)

    return output

def findContours(image):
    # Frame capture need to be in gray scale in order to threshold image
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    # Paramaters:
    # 1. source image
    # 2. threshold value: Pixels greater than 127 will converted to black 255
    #                  Pixels less than 127 will converted to white
    # 3. Max color value 255 black
    # 4. Amount of channels in the image. Grayscale image only has one channel or color intensity.
    # Returns threshold-ed imaga
    ret,thresh = cv2.threshold(grayscale,80,255,0)


    # Parameters:
    # 1. source image
    # 2. Contour retrieval mode used
    # 3. Contour approximation method used
    # Returns a list contour object. A contour object contain info on each point that make up the contour
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    return contours

def distFromCenter(image, point):
    height, width, channels = image.shape
    center = Point(width/2-point.getX(), height/2-point.getX())
    return center

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return [self.x, self.y]

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def toTuple(self):
        return (self.x, self.y)
		
class Circle:

	def __init__(self, x=0, y=0, radius=0):
		self.radius = radius
		self.point = Point(x,y)
		
	def getX(self):
		return self.point.getX()

	def getY(self):
		return self.point.getY()
	
	def getRadius(self):
		return self.radius
	
	def getPoint(self):
		return self.point
	
	def __repr__(self):
		return [self.x, self.y, self.radius]
		
	def toArray(self):
		return [self.point.getX(), self.point.getY(), self.radius]
	

def colorCalibrate(color):
    print "This is the color calibration program. Press (a,z,s,x,d,c,f,v,g,b)"
    print "Keys: a,z,s,x,d,c are for the upperbound configuration"
    print "top row is for raising the value"
    print "bottom row is for lowering the value"
    print "Keys: f,v,g,b,h,n are for the lower configuration"
    print "top row is for raising the value"
    print "bottom row is for lowering the value"

    input_queue = Queue.Queue()
    thread = threading.Thread(target=calibrate, args=(input_queue, color))
    thread.daemon = True
    thread.start()

def calibrate(queue, color):
    while True:
        try:
            letter = sys.stdin.read(1)
            if letter != '\n':
                queue.put(parse_letter(letter))
        except KeyError:
            print "Bad key!"

        if not queue.empty():
            direction, bound, channel = queue.get()
            print "--"
            print color
            color[bound][channel] += (direction * INREMENT_VALUE)
            print color


