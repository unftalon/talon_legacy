from time import sleep
import cv2

# WARNING: Code will fail if adequate time is not given between frame captures
# 2 decisecond
READ_DELAY = 0.2
class Camera:
          # getVideoSettings arguments
      # fileName: to save the *.avi file to
      # fps: frames per second e.g 12 fps, 30 fps
      # size: width and height of frame, best to get it from frame!
      # getVideoSettins return
      # videoSettings: This is actually the videoWriter.
   def getVideoSettings(self,fileName, fps, size):
    videoSettings = cv2.VideoWriter(fileName, cv2.cv.CV_FOURCC(*'XVID'), fps, size)
    return videoSettings

          #recordFrame arguments
      # frame: video capture
      # videoWriter: Writes frame to *.avi file specified
   def recordFrame(self, frame, videoWriter):
    videoWriter.write(frame)

   def getFrameSize(self):
    size = (int(self.cv_camera.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
    int(self.cv_camera.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
    return size

   def getFrame(self):
      sleep(READ_DELAY)
      ret, frame = self.cv_camera.read()
      return frame

   def __init__(self,cv2, isBaseCamera = 0):
      self.cv_camera = cv2.VideoCapture(isBaseCamera)

