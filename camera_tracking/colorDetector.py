# import function, variable, and classes from other modules  
import numpy as np
import cv2
from ospery_diver import Camera, Display, Executor, tasks
from ospery_diver.util import *


cam = Camera(cv2)              # Camera Object
display = Display(cv2)         # Object used to display results or camera frames
executor = Executor(cv2, np)   # The object that is responsible for executing different tasks (color detection, buoy detection, etc )

# Program we will be constantly looping 
# press CTRL-C to abort (end program) 
while( True ):

    frame = cam.getFrame()    # get a single frame or image from the camera and store it in a object

    # Try running the task with different colors
    # Comment the color = ORANGE and uncomment either color = BLUE or color GREEN 
    color = ORANGE
    #color = BLUE
    #color = GREEN


    buoyTask = executor.run(tasks.buoyDetector, frame, color)   # Execute the task. The executed task can be stored in variable     
	
    buoyResult = buoyTask.result()    # grab a result object from the task 
    buoyResult.drawOnFrame(frame)     # the result  of the task can draw on the frame 

    # comment the if block below and uncomment the other if block to see the thresholded frame
    if (display.show(frame, "output")==-1):

        display.destroy()	

    #if (display.show(buoyTask.getThresholdFrame(), "output")==-1):

    #    display.destroy()
