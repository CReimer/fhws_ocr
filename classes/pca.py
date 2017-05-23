import numpy
import cv2


class PCA:
    def __init__(self):
        self.matrix = []
        pass

    def trainChar(self, char, img_arr):
        for img in img_arr:

            resized = cv2.resize(img, (100, 100), interpolation=cv2.INTER_AREA)

            imgvector = self.generateRowVector(resized)  # Use own implementation
            self.matrix.append(imgvector)

    @staticmethod
    def generateRowVector(img):
        (lines, rows) = img.shape
        rowvector = []
        for row in range(rows):
            for line in range(lines):
                rowvector.append(img[line][row])
        return rowvector

    def generateMeanPerLine(self):
        longestLine = 0
        for row in self.matrix:
            if len(row) > longestLine:
                longestLine = len(row)
        meansPerLine = [0.0] * longestLine

        for row in range(len(self.matrix)):
            for line in range(longestLine):
                try:
                    if self.matrix[row][line]:
                        meansPerLine[line] += self.matrix[row][line]
                except IndexError or TypeError:
                    pass

        for line in range(len(meansPerLine)):
            meansPerLine[line] /= len(self.matrix)

        return meansPerLine

    def shiftByMean(self, means):
        for row in range(len(self.matrix)):
            for line in range(len(self.matrix[row])):
                self.matrix[row][line] -= means[line]

    def pca(self):
        matrix = numpy.array(self.matrix)

        from matplotlib.mlab import PCA as mlabPCA
        mlab_pca = mlabPCA(matrix.T)
        print(mlab_pca.Y.T[0, 0])
        print(mlab_pca.Y.T[1, 0])
