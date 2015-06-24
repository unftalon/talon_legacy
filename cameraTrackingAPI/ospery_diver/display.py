from util import *

class Display:

	def show(self, image, label=None):
		if label == None:

			self.cv2.imshow(str(self.counter), image)
			self.counter+=1
		else:
			self.cv2.imshow(label, image)

        # Waitkey will display image 1 ms until.
        # After 1 ms if a key is pressed the window will terminate (break loop)
		if self.cv2.waitKey(1) & 0xFF == ord('q'):
			destroy()
			return -1

	def destroy(self):
		self.cv2.destroyAllWindows()

   	def __init__(self, cv2):
		self.cv2 = cv2
		self.counter = 0

	def drawCircle(self, image, point, radius, color=RED, thickness=5):
		self.cv2.circle(image, point.toTuple(), radius, color, thickness)

	def drawContour(self, image, rect, color, thickness):
		self.cv2.drawContours(image, [rect], 0, color, thickness)

	def putText(self, image, text, point, color=RED, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.5, font_thickness=2):
		cv2.putText(image, text, point.toTuple(), font, font_scale, RED, font_thickness)
