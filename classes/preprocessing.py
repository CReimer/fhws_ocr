import cv2


class Preprocessing:
    def __init__(self, img):
        self.img = img
        self.rows = len(img[0])
        self.lines = len(img)

        # Contrast stretch

        # for line in range(len(self.img)):
        #     for row in range(len(self.img[line])):
        #         self.img[line][row] = (self.img[line][row] - self.img.min()) / (self.img.max() - self.img.min()) * 255

        # ret, self.img = cv2.threshold(self.img, 127, 255, cv2.THRESH_BINARY)
        # ret, self.img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
        # ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
        # ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
        # ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

        # row_info = [None] * self.rows
        # for row in range(self.rows):
        #     single = 0
        #     for line in range(self.lines):
        #         single += self.img[line][row]
        #     row_info[row] = single

        # print('dd')

    def binariseImg(self):
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

    def splitChars(self):
        rowOccupancy = [None] * self.rows
        for row in range(self.rows):
            singleOcc = 0
            for line in range(self.lines):
                if self.img[line][row] == 0:
                    singleOcc += 1
            rowOccupancy[row] = singleOcc

        print("dd1")

        occupancyThres = 2

        chars = []
        temp_counter = 0
        cur_row = 0
        start_row = None
        end_row = None
        while cur_row < self.rows:
            if start_row and end_row:
                temp_counter += 1

                chars.append(self.img[0:30, start_row:end_row])

                start_row = None
                end_row = None

                # cur_row += 1
                continue

            if start_row:
                if rowOccupancy[cur_row] <= occupancyThres:
                    end_row = cur_row
            else:
                if rowOccupancy[cur_row] > occupancyThres:
                    start_row = cur_row

            cur_row += 1

        print("dd2")

        for idx in range(len(chars)):
            cv2.imwrite("single" + str(idx) + '.jpg', chars[idx])

    def showImage(self):
        cv2.imshow('Preprocessing', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
