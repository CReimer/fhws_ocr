import cv2


class Preprocessing:
    def __init__(self, img):
        print("Init Preprocessing")
        self.img = img
        self.rows = len(img[0])
        self.lines = len(img)

    def stretchContrast(self):
        print("Stretching contrast")
        for line in range(len(self.img)):
            for row in range(len(self.img[line])):
                self.img[line][row] = (self.img[line][row] - self.img.min()) / (self.img.max() - self.img.min()) * 255

    def binariseImg(self):
        print("Binarising image")
        ret, img = cv2.threshold(self.img, 127, 255, cv2.THRESH_BINARY)

        # Check if inversion is necessary
        black = 0
        white = 0
        for line in range(len(img)):
            for row in range(len(img[line])):
                if img[line][row] == 255:
                    white += 1
                else:
                    black += 1

        if black > white:
            ret, img = cv2.threshold(self.img, 127, 255, cv2.THRESH_BINARY_INV)

        self.img = img

    # Trennung an Spalten mit 0 Pixeln
    def splitChars(self, occupancyThres=0):
        print("Splitting characters")

        # Zähle genutze Pixel in allen Spalten
        rowOccupancy = [None] * self.rows
        for row in range(self.rows):
            singleOcc = 0
            for line in range(self.lines):
                if self.img[line][row] == 0:
                    singleOcc += 1
            rowOccupancy[row] = singleOcc

        chars = []
        cur_row = 0
        start_row = None
        end_row = None
        while cur_row < self.rows:
            if start_row and end_row:
                chars.append(self.img[0:self.lines, start_row:end_row])

                start_row = None
                end_row = None

                continue

            if start_row:
                if rowOccupancy[cur_row] <= occupancyThres:
                    end_row = cur_row
            else:
                if rowOccupancy[cur_row] > occupancyThres:
                    start_row = cur_row

            cur_row += 1

        # for idx in range(len(chars)):
        #     cv2.imwrite("single" + str(idx) + '.jpg', chars[idx])
        return chars


