import numpy as np
import cv2
from ospery_diver import Camera, Display, Executor, tasks
from ospery_diver.util import *
import Queue
import threading

cam = Camera(cv2)
display = Display(cv2)
executor = Executor(cv2, np)

input_queue = Queue.Queue()
thread = threading.Thread(target=calibrate, args=(input_queue,))
thread.daemon = True
thread.start()

while (True):
    if not input_queue.empty():
        direction, bound, channel = input_queue.get()
        print "--"
        print BLAZEORANGE
        BLAZEORANGE[bound][channel] += (direction * INREMENT_VALUE)
        print BLAZEORANGE


    frame = cam.getFrame()
    rects = executor.run(tasks.findBoundingRectsByColor, frame, BLAZEORANGE)
    for rect in rects:
        display.drawContour(frame, rect, RED, 2)
    if (display.show(frame, "output")==-1):
        break
