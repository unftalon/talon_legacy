from util import *

class Display:

    def show(self, image, label):
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

    def putText(self, image, text, point, color=RED, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.5, font_thickness=2):
        cv2.putText(image, text, (point[0],point[1]), font, font_scale, RED, font_thickness)
