import numpy
from matplotlib.mlab import PCA


class PCA:
    def __init__(self):
        pass

    def trainChar(self, char, img_arr):
        matrix = []  # Will be multidimensional -> [rows][lines]
        for img in img_arr:
            matrix.append(self.generateRowVector(img))

        self.generateMeanPerLine(matrix)

    @staticmethod
    def generateRowVector(img):
        (lines, rows) = img.shape
        rowvector = []
        for row in range(rows):
            for line in range(lines):
                rowvector.append(img[line][row])
        return rowvector

    @staticmethod
    def generateMeanPerLine(matrix):
        longestLine = 0
        for row in matrix:
            if len(row) > longestLine:
                longestLine = len(row)
        meansPerLine = [0.0] * longestLine

        for row in range(len(matrix)):
            for line in range(longestLine):
                try:
                    if matrix[row][line]:
                        meansPerLine[line] += matrix[row][line]
                except IndexError or TypeError:
                    pass

        for line in range(len(meansPerLine)):
            meansPerLine[line] /= len(matrix)

        return meansPerLine

# Flo's Part___

    def shiftingByMean(self, matrix):
        means = self.generateMeanPerLine(matrix)
        for row in matrix:
            for line in matrix[row]:
                matrix[row][line] -= means[line]
        return matrix

    def mlabPCA(self, matrix):
        # mlab's PCA expects a 2d numpy Array
        myData = numpy.array(matrix)
        results = PCA(myData)

        #this will return an array of variance percentages for each component
        results.fracs

        #this will return a 2d array of the data projected into PCA space
        results.Y

        return results.Y

