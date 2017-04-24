import cv2


class Tools:
    def __init__(self):
        print("Init Tools")

    @staticmethod
    def showImage(img):
        cv2.namedWindow('Preprocessing', cv2.WINDOW_NORMAL)
        cv2.imshow('Preprocessing', img)
        cv2.resizeWindow('Preprocessing', 600, 600)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def writeImage(img, name='out.png'):
        cv2.imwrite(name, img)
