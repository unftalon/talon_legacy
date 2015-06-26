import cv2
from util import *
from ospery_diver import Display
from ospery_diver import PointTaskResult
from ospery_diver import RectangeCollectionTaskResult
from ospery_diver import UnsuccessfulTaskResult

class GateDetectorTask:
    def __init__(self,cv2, np, image, color):
        self.cv2 = cv2
        # The frame capture is in RGB (Red-Blue-Green)
        # It need to be in HSV (Hue Saturation and Value) in order for opencv to perform color detection
        hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


        # Return the image with just the detected color
        detected = detectColor(hsv_img, color)

        # Find the contours
        contours = findContours(detected)

        if len(contours) > 0:
            points = []
            for contour in contours:
                moments = cv2.moments(contour)

                if(moments['m00']):

                    # For each contour detected, find the center
                    points.append([moments['m10']/moments['m00'] ,moments['m01']/moments['m00']])

            if len(points) == 0:
                return None

            points = np.array(points)
            points = np.float32(points)
            term_crit = (cv2.TERM_CRITERIA_EPS, 40, 0.1)

            ret, labels, centers = cv2.kmeans(points, 1, term_crit, 40, 0)
            self.coordinates = (int(centers[0,0]), int(centers[0,1]))
            self.detected = detected

    def result(self):
        if(not hasattr(self, 'coordinates')):
            return UnsuccessfulTaskResult(self.cv2)
        return PointTaskResult(self.cv2, self.coordinates)

    def getThresholdFrame(self):
        return self.detected

class FindBoundingRectsByColorTask:
    def __init__(self, cv2, np, image, color):
        # The frame capture is in RGB (Red-Blue-Green)
        # It need to be in HSV (Hue Saturation and Value) in order for opencv to perform color detection
        hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Return the image with just the detected color
        detected = detectColor(hsv_img, color)

        str_el = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        detected = cv2.morphologyEx(detected, cv2.MORPH_OPEN, str_el);
        detected = cv2.morphologyEx(detected, cv2.MORPH_CLOSE, str_el);

        # Find the contours
        contours = findContours(detected)

        rects = []

        for contour in contours:

            rect = cv2.minAreaRect(contour)
            box = cv2.cv.BoxPoints(rect)
            box = np.int0(box)
            rects.append(box)
        self.rects = rects
        self.cv2 = cv2
        self.detected = detected

    def result(self):
        return RectangeCollectionTaskResult(self.cv2, self.rects)

    def getThresholdFrame(self):
        return self.detected

def gateDetector(cv2, np, image, color):
    return GateDetectorTask(cv2, np, image, color)

def findBoundingRectsByColor(cv2, np, image, color):
    return FindBoundingRectsByColorTask(cv2, np, image, color)
