import cv2
from util import *
from ospery_diver import Display

def blazed_orange():
    return BLAZEORANGE

def gateDetector(cv2, np, image, color):

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
        
        
        return Point(int(centers[0,0]),int(centers[0,1]))
        

    else:

        return None



def findBoundingRectsByColor(cv2, np, image, color):

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

    return rects
