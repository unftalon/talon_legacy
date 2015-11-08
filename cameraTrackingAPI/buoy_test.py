import numpy as np
import cv2
from ospery_diver import Camera, Display, Executor, tasks, Communicator
from ospery_diver.util import *
import time

cam = Camera(cv2)
display = Display(cv2)
executor = Executor(cv2, np)
# for video logging please donot erase!
# fps = 13
# size = cam.getFrameSize()
# fwdCamFileName = 'fwdCamera.avi'
# videoWriter = cam.getVideoSettings(fwdCamFileName,fps,size)
# numFramesRemaining = 10 * fps - 1
colorCalibrate(all_colors())

while( True ):

	frame = cam.getFrame()

	buoyTask = executor.run(tasks.buoyDetector, frame, orange())
	
	buoyResult = buoyTask.result()
	buoyResult.drawOnFrame(frame)
	
	display.show(buoyTask.getThresholdFrame(), "buoy_threshold")
	
	#rectResult = executor.run(tasks.findBoundingRectsByColor, frame, ORANGE)
	#rectResult.result().drawOnFrame(frame)
	
    
	
	

	if (display.show(frame, "output")==-1):
		break

    #while numFramesRemaining > 0:
        #cam.recordFrame(frame, videoWriter)
        #frame = cam.getFrame()
        #numFramesRemaining -= 1

display.destroy()
