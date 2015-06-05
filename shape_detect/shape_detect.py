import numpy as np
import cv2
from time import sleep
x# WARNING: Code will fail if adequate time is not given between frame captures
# 1 decisecond
READ_DELAY = 0.1

FONT = cv2.FONT_HERSHEY_SIMPLEX

GREEN = (0, 255, 0)

ORANGE = (0, 128, 255)

RED = (0, 0, 255)

CYAN = (255,255,0)

FONT_SCALE = 0.5

THINKNESS  = 2

THRESHOLD_VALUE = 127

MAX_THRESHOLD_VALUE = 255

GRAYSCALE_CHANNELS = 1 

CV_RETR_LIST = 1

CV_CHAIN_APPROX_SIMPLE = 2

shapes = {'rectangle': 4, 'triangle': 3};


# Find contours within frame
# Contour is just a fancy of way saying the outline or 
# bounding shape of a 2D projection of an object
def detectContours(frame):

    # Frame capture need to be in gray scale in order to threshold image
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Paramaters:
    # 1. source image
    # 2. threshold value: Pixels greater than 127 will converted to black 255
    #                  Pixels less than 127 will converted to white
    # 3. Max color value 255 black 
    # 4. Amount of channels in the image. Grayscale image only has one channel or color intensity. 
    # Returns threshold-ed imaga
    ret, thresh = cv2.threshold(grayscale,THRESHOLD_VALUE,MAX_THRESHOLD_VALUE,GRAYSCALE_CHANNELS)

    # Parameters:
    # 1. source image
    # 2. Contour retrieval mode used
    # 3. Contour approximation method used
    # Returns a list contour object. A contour object contain info on each point that make up the contour
    contours,h = cv2.findContours(thresh,1,2)

    return contours

# Take the list of contours and draw them on the frame
def drawContours(frame, contours):

    # Iterate through each contour
    for contour in contours:

        # Approximate the contour (smoooth it out) so can tell if is a fundamental shape (rectangle, triangle, circle)
        # Paramater
        # 1. contour can also be seen as a list of points for a closed curve
        # 2. epsilon: specify the approximation accuracy . maximum distance between the original curve and its approximation
        # 3. Boolean is to used specify if the curve that we are dealing with is closed is closed. 
        # Returns a list points representing a smoother contour
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)

        for shape, edges in shapes.iteritems():

            if len(approx)==edges: 
                cv2.drawContours(frame,[contour],0,CYAN,-1)
                break




def init():

    # Video Camera Object
    cam = cv2.VideoCapture(0)

    while(True):

    	# Wait a specified amount of time prior to fram capture
        sleep(READ_DELAY)

        # Capture frame-by-frame
        ret, frame = cam.read()

        drawContours(frame, detectContours(frame))

        cv2.imshow("output", frame)


        # Waitkey will display image 1 ms until. 
        # After 1 ms if a key is pressed the window will terminate (break loop)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

init()
