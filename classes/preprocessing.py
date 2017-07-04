import cv2
import numpy


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
        ret, img = cv2.threshold(self.img, 127, 255, cv2.THRESH_BINARY)
        # img = cv2.adaptiveThreshold(self.img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c)

        # Check if inversion is necessary
        black = 0
        white = 0
        for line in range(len(img)):
            for row in range(len(img[line])):
                if img[line][row] == 255:
                    white += 1
                else:
                    black += 1

        if black < white:
            img = (255 - img)

            self.img = img

    # Trennung an Spalten mit 0 Pixeln
    def splitChars(self):
        print("Splitting characters")
        chars = []

        rowOccupancy = [0] * self.rows
        for row in range(self.rows):
            for line in range(self.lines):
                if self.img[line][row] > 0:
                    rowOccupancy[row] += 1

        start_row = None
        end_row = None

        margin_percent = 0.0
        margin = line / 100 * margin_percent

        for row in range(len(rowOccupancy)):
            if start_row:
                if rowOccupancy[row] <= margin:
                    end_row = row
            else:
                if rowOccupancy[row] > margin:
                    start_row = row

            if start_row and end_row:
                img = self.splitTopBottom(self.img[0:self.lines, start_row:end_row])
                chars.append(img)

                # Reset
                start_row = None
                end_row = None

        return chars

    def splitTopBottom(self, img):
        (lines, rows) = img.shape

        lineOccupancy = [0] * self.lines
        for line in range(lines):
            for row in range(rows):
                if img[line][row] > 0:
                    lineOccupancy[line] += 1

        start_line = None
        end_line = None
        for line in range(len(lineOccupancy)):
            if not start_line:
                if lineOccupancy[line]:
                    start_line = line
            if lineOccupancy[line]:
                end_line = line
        return img[start_line:end_line, 0:rows]

    def skelettizeImg(self):
        skel = numpy.zeros(self.img.shape, numpy.uint8)  # Initialize empty skeleton
        element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))  # Define erode and dilate behaviour
        size = numpy.size(self.img)  # Pixel count
        black_pixels = 0  # Initialize with zero

        # Break if there are only black pixels (background)
        while not black_pixels == size:
            eroded = cv2.erode(self.img, element)  # Slim picture down by one pixel
            dilated = cv2.dilate(eroded, element)  # Use slimmed down picture and increase thickness by one pixel
            # With this process we have removed possible unique features of a character

            remain = cv2.subtract(self.img,
                                  dilated)  # Subtract dilated img from source img. Only unique features remain here
            skel = cv2.bitwise_or(skel, remain)  # Append these unique features to our skeleton image
            self.img = eroded.copy()  # Use the slimmed down picture for next loop run

            black_pixels = size - cv2.countNonZero(self.img)  # Number of black pixels

        self.img = skel
