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
        block_size = 11  # decides the size of neighbourhood area
        c = -10  # a constant which is subtracted from the mean or weighted mean
        print("Binarising image")
        # img = cv2.adaptiveThreshold(self.img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c)
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
            img = (255 - img)

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
        cur_row = -1
        start_row = None
        end_row = None
        while cur_row < self.rows:
            cur_row += 1
            if start_row and end_row:
                chars.append(self.img[0:self.lines, start_row:end_row])

                start_row = None
                end_row = None

                continue

            try:
                if start_row:
                    if rowOccupancy[cur_row] <= occupancyThres:
                        end_row = cur_row
                else:
                    if rowOccupancy[cur_row] > occupancyThres:
                        start_row = cur_row
            except IndexError:
                break

        return chars
#