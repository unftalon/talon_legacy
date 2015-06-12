import numpy as np
import time
import cv2
from time import sleep
# WARNING: Code will fail if adequate time is not given between frame captures
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

def method():
  # define the upper and lower boundaries for a color
  # to be considered "blue"
  blueLower = np.array([14,65,183], dtype = "uint8")
  blueUpper = np.array([81,116,233], dtype = "uint8")
  
  # load camera
  camera = cv2.VideoCapture(0)
  
  #keep looping
  while True:
    # grab the current frame
    (grabbed, frame) = camera.read()
  
    # check to see if we have reached the end of the video
    if not grabbed:
      break
  
    # determine which pixels fall within the blue boundaries
    # and then blur the binary image
  
    blue = cv2.inRange(frame, blueLower, blueUpper)
    blue = cv2.GaussianBlur(blue, (3, 3), 0)
  
    # find contours in the image
    (cnts, _) = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE)
  
    # check to see if any contours were found

    if len(cnts) > 0:
      # sort the contours and find the largest one -- we
      # will assume this contour correspondes to the area
      # of object
      sorted_cnts = sorted(cnts, key = cv2.contourArea, reverse = True)
      displayed_rectangles = 0
      for cnt in sorted_cnts:
        # compute the (rotated) bounding box around then
        # contour and then draw it
        rect = np.int32(cv2.cv.BoxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)
        displayed_rectangles = displayed_rectangles + 1
        if displayed_rectangles >= 2:
            break
                    
    # show the frame and the binary image
    cv2.imshow("Tracking", frame)
    cv2.imshow("Binary", blue)
  
    # if your machine is fast, it may display the frames in 
    # what appears to be 'fast forward' since more than 32
    # frames per second are being displayed -- a simple hack
    # is just to sleep for a tiny bit in between frames;
    # however, if  raspberry is slow,  comment out the line
    time.sleep(0.025)
    
    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break
  
  # cleanup the camera and close any open windows
  camera.release()
  cv2.destoryAllWindows()

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
    print "hello"
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
 
