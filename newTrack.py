import numpy as np
import time
import cv2
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
			cnt = sorted_cnts[0]
			cnt2 = sorted_cnts[1]
	
			# compute the (rotated) bounding box around then
			# contour and then draw it
			rect = np.int32(cv2.cv.BoxPoints(cv2.minAreaRect(cnt)))
                        rect2 = np.int32(cv2.cv.BoxPoints(cv2.minAreaRect(cnt2)))

			cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)
			cv2.drawContours(frame, [rect2], -1, (0, 255, 0), 2)
	                  
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
