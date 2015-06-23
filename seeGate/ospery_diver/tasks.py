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

    cv2.imshow("detected", detected)
    
    rects = findBoundingRectsByColor(cv2, np, detected, color)

    points = []
    if len(rects) > 0:
        for rect in rects:
            for point in rect:
                
                points.append(point)

        points = np.array(points)
        points = np.float32(points)
        center = getCenter(points)
        
        return center
        
  
      
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
