import cv2


class Preprocessing:
    def __init__(self, img):
        self.img = img

    def doSomething(self):
        self.img = cv2.Canny(self.img,100,200)

    def showImage(self):
        cv2.imshow('Preprocessing', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
