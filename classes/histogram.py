import cv2


class Histogram:
    def __init__(self, img):
        print("Init Preprocessing")
        self.img = img
        self.rows = len(img[0])
        self.lines = len(img)

    # Histogramm für die rows

    def runterfallen(self):

        f = []
        for row in range(len(self.img)):
            count = 0
            for line in range(len(self.img[row])):
                if self.img[line][row] == 255:
                    count = count + 1
            f.append(row, count)
        return f

    # Histogramm für die lines

    def zurseiterutschen(self):

        f = []
        for line in range(len(self.img)):
            count = 0
            for row in range(len(self.img[line])):
                if self.img[line][row] == 255:
                    count = count + 1
            f.append(line, count)
        return f
#
