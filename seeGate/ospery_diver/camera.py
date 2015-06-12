from time import sleep

# WARNING: Code will fail if adequate time is not given between frame captures
# 2 decisecond
READ_DELAY = 0.2

class Camera:

   def getFrame(self):
      sleep(READ_DELAY)
      ret, frame = self.cv_camera.read()
      return frame

   def __init__(self,cv2):
      self.cv_camera = cv2.VideoCapture(0)

