import numpy as np
import cv2
from ospery_diver import Camera, Display, Executor, tasks
from ospery_diver.util import *

if __name__ == '__main__':

	cam = Camera(cv2)
	display = Display(cv2)
	executor = Executor(cv2, np)

	while( True ):

		frame = cam.getFrame()
		
		#point = executor.run(tasks.gateDetector, cam.getFrame())


		#if point is not None:

			#draw a cross hair
		#	cv2.circle(frame, (point.getX() ,point.getY()), 40, (0,0,255), 5)

		print frame
		rects = executor.run(tasks.findBoundingRectsByColor, cam.getFrame(), ORANGE)

		for rect in rects:
			display.drawContour(frame, rect, RED, 2)

		if (display.show(frame, "output")==-1):
			break

	display.destroy()
