import numpy as np
import cv2
from ospery_diver import Camera, Display, Executor, tasks
from ospery_diver.util import *

if __name__ == '__main__':

	cam = Camera(cv2)
	display = Display(cv2)
	executor = Executor(cv2, np)
	# for video logging please donot erase!
	fps = 13
	size = cam.getFrameSize()
	fwdCamFileName = 'fwdCamera.avi'
        videoWriter = cam.getVideoSettings(fwdCamFileName,fps,size)
	numFramesRemaining = 10 * fps - 1
	while( True ):

		frame = cam.getFrame()
		
		while numFramesRemaining > 0:
			cam.recordFrame(frame, videoWriter)
			frame = cam.getFrame()
			numFramesRemaining -= 1
		
		#point = executor.run(tasks.gateDetector, cam.getFrame())


		#if point is not None:

			#draw a cross hair
		#	cv2.circle(frame, (point.getX() ,point.getY()), 40, (0,0,255), 5)

		#rects = executor.run(tasks.findBoundingRectsByColor, cam.getFrame(), ORANGE)

		#for rect in rects:
			#display.drawContour(frame, rect, RED, 2)

		if (display.show(frame, "output")==-1):
			break

	display.destroy()
