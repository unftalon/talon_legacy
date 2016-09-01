import numpy as np
import cv2
from ospery_diver import Camera, Display, Executor, tasks, Communicator
from ospery_diver.util import *
import time

cam = Camera(cv2)
display = Display(cv2)
executor = Executor(cv2, np)


while( True ):

	frame = cam.getFrame()

	task = executor.run(tasks.gateDetector, frame, orange(), [histogramStrenching])
	
	result = task.result()
	result.drawOnFrame(frame)
	
	
	#rectResult = executor.run(tasks.findBoundingRectsByColor, frame, orange())
	#rectResult.result().drawOnFrame(frame)
	
    
	
	

	if (display.show(frame, "output")==-1):
		break

    #while numFramesRemaining > 0:
        #cam.recordFrame(frame, videoWriter)
        #frame = cam.getFrame()
        #numFramesRemaining -= 1

display.destroy()