import cv2


class Histogram:
    def __init__(self, img):
        print("Init Histogram")
        self.img = img
        self.rows = len(img[0])
        self.lines = len(img)

    # Histogramm für die rows

    def runterfallen(self):

        f = []
        for row in range(len(self.img)):
            count = 0
            for line in range(len(self.img[row])):
                if self.img[row][line] == 0:
                    count = count + 1
            f.append(count)
        return f

    # Histogramm für die lines

    def zurseiterutschen(self):

        f = []
        for line in range(len(self.img)):
            count = 0
            for row in range(len(self.img[line])):
                if self.img[line][row] == 0:
                    count = count + 1
            f.append(count)
        return f
#
