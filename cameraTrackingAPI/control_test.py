import numpy as np
import cv2
from ospery_diver import Camera, Display, Executor, tasks, Communicator
from ospery_diver.util import *
import time

cam = Camera(cv2)
display = Display(cv2)
executor = Executor(cv2, np)
comm = Communicator('COM4', 9600)
# for video logging please donot erase!
# fps = 13
# size = cam.getFrameSize()
# fwdCamFileName = 'fwdCamera.avi'
# videoWriter = cam.getVideoSettings(fwdCamFileName,fps,size)
# numFramesRemaining = 10 * fps - 1
#colorCalibrate(all_colors())


task_name=""



def idlePhase():
	
	task_num = comm.standBy() 			# Awaiting orders from the arduino. 
	task = tasks.TASKS[task_num]	  	# A single number will represent an index of task in the TASKS array
	task_name = task.__name__
	print task_name
	runTask(task)			 			# run the task
	
def runTask(task):
	
	while True:
				
		executed = executor.run(task, cam.getFrame(), ORANGE)
		result = executed.result()
		thresholdedFrame = executed.getThresholdFrame()
		
	
		if (display.show(thresholdedFrame, "thresholded")==-1):
			break
		
		
		frame = cam.getFrame()
		result.drawOnFrame(frame)
		display.putText(frame, task_name, Point(0, 0))	# Display name of current task being perform
		
		if (display.show(frame, "output")==-1):
			break
			
		value = result.arrayValue()
		if value is not None:
			
			# A success in this case will be how far the detected object is away from the center/orgin Point(0,0)
			if isCentered(value[0], value[1], frame, 100):	
				comm.sendSuccess()
				idlePhase()

idlePhase()
	
	
