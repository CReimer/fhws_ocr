class Histogram:
    def __init__(self, img):
        print("Init Histogram")
        self.img = img
        self.rows = len(img[0])
        self.lines = len(img)

    def row_histogram(self):

        f = []
        for row in range(len(self.img)):
            count = 0
            for line in range(len(self.img[row])):
                if self.img[row][line] == 0:
                    count = count + 1
            f.append(count)
        return f

    def line_histogram(self):

        f = []
        for line in range(len(self.img)):
            count = 0
            for row in range(len(self.img[line])):
                if self.img[line][row] == 0:
                    count = count + 1
            f.append(count)
        return f

    def rowWert2wert(self):
        f = []

        rowlength = len(self.img[0])
        linelength = len(self.img)
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for row in range(rowlength):

            if self.img[0][row] == 0:
                count1 = count1 + 1
            if self.img[linelength - 1][row] == 0:
                count2 = count2 + 1

        for line in range(linelength):

            if self.img[line][0] == 0:
                count3 = count3 + 1
            if self.img[line][rowlength - 1] == 0:
                count4 = count4 + 1

        f.append(count1)
        f.append(count2)
        f.append(count3)
        f.append(count4)
        return f


