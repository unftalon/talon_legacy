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
colorCalibrate(all_colors())

MARGIN_FROM_CENTER = 150
task_name=""

def idlePhase():

	task_num = comm.standBy()
	task = tasks.getTaskByNum(task_num)
	task_name = task.__name__
	runTask(task)
	
def runTask(task):
	
	while True:
	
		frame = cam.getFrame()
		
	
		if (display.show(frame, "output")==-1):
			break
			
		executed = executor.run(task, cam.getFrame(), all_colors())
		result = executed.result()
		result.drawOnFrame(frame)
		thresholdedFrame = executed.getThresholdFrame()
		
		if thresholdedFrame is not None:
			if (display.show(thresholdedFrame, "thresholded")==-1):
				break
		
		value = result.arrayValue()
		print value
		if value is not None:
			if isCentered(value[0], value[1]):
				comm.sendSuccess()
				idlePhase()
				
def isCentered(x, y):
	point = distFromCenter(cam.getFrame(),Point(x,y))
	if abs(point.getX()) <= MARGIN_FROM_CENTER and abs(point.getY()) <= MARGIN_FROM_CENTER:
		return True
	else:
		return False

idlePhase()
	
	
