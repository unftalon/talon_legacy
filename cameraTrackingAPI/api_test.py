import numpy as np
import cv2
from ospery_diver import Camera, Executor, tasks, Communicator
from ospery_diver.util import *
import time

cam = cv2.VideoCapture(0)
executor = Executor(cv2, np)
comm = Communicator('/dev/ttyAMA0', 9600)
# calibrated_color = long_range_orange()
# colorCalibrate(calibrated_color)
# display = Display(cv2)
ret, frame = cam.read()
height, width, _ = frame.shape
mid_x = width / 2
mid_y = height / 2
i = 0

turn = False
while( True ):
    i += 1
    ret, frame = cam.read()
    cv2.imwrite('/home/pi/test' + str(i) + '.jpg', frame)
    pointTask = executor.run(tasks.gateDetector, frame, orange())
    pointResult = pointTask.result()
    pointResult.drawOnFrame(frame)
    
    # display.show(frame, 'frame')
    # display.show(threshold, 'threshold')
    command = "1 1 "
    if pointResult.value() is not None:
        gate_x = pointResult.value()[0]
        gate_y = pointResult.value()[1]

        if gate_y < mid_y:
            command += "2 1"
        else:
            command += "2 3"

        turn = False
        if gate_x > mid_x:
            command += " 3 3" # left
            turn = True
        if gate_x < mid_x:
            command += " 3 4" # right
            turn = True
    else:
        print "None"

    if turn == False:
        command = "3 0 1 1" # no turn
        print "no turn"
    print command
    comm.writeln(command)
