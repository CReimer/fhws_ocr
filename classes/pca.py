import numpy
from matplotlib.mlab import PCA as matplot_pca
from classes.database import Database


class PCA:
    def __init__(self):
        pass

    def trainChar(self, char, img_arr):
        matrix = []  # Will be multidimensional -> [rows][lines]
        for img in img_arr:
            matrix.append(self.generateRowVector(img))

        means = self.generateMeanPerLine(matrix)
        newMatrix = self.shiftByMean(matrix, means)
        pcaResult = self.mlabPCA(newMatrix)

        database = Database()
        database.add(char, 'pca', pcaResult)

        print(pcaResult)

    @staticmethod
    def compareChar():
        # TODO
        return True

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

    @staticmethod
    def shiftByMean(matrix, means):
        for row in range(len(matrix)):
            for line in range(len(matrix[row])):
                matrix[row][line] -= means[line]
        return matrix

    @staticmethod
    def mlabPCA(matrix):
        # mlab's PCA expects a 2d numpy Array
        myData = numpy.array(matrix)
        myData = myData.T  # We have to transpose the matrix here. Matplot expects [line][row] and we have [row][line]
        results = matplot_pca(myData)

        # this will return an array of variance percentages for each component
        # return results.fracs

        # this will return a 2d array of the data projected into PCA space
        return results.Y
