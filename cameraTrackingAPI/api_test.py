import numpy as np
import cv2
from ospery_diver import Camera, Display, Executor, tasks
from ospery_diver.util import *

cam = Camera(cv2)
display = Display(cv2)
executor = Executor(cv2, np)
# for video logging please donot erase!
# fps = 13
# size = cam.getFrameSize()
# fwdCamFileName = 'fwdCamera.avi'
# videoWriter = cam.getVideoSettings(fwdCamFileName,fps,size)
# numFramesRemaining = 10 * fps - 1
while( True ):
    frame = cam.getFrame()

    pointResult = executor.run(tasks.gateDetector, frame, orange())
    pointResult.result().drawOnFrame(frame)

    rectResult = executor.run(tasks.findBoundingRectsByColor, frame, orange())
    rectResult.result().drawOnFrame(frame)

    display.show(rectResult.getThresholdFrame(), "rect_threshold")

    if (display.show(frame, "output")==-1):
        break

    #while numFramesRemaining > 0:
        #cam.recordFrame(frame, videoWriter)
        #frame = cam.getFrame()
        #numFramesRemaining -= 1

display.destroy()
