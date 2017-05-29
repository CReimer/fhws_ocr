import numpy as np
import cv2
from scipy.sparse.linalg import eigs, eigsh


class PCA:
    def __init__(self):
        self.matrix = []
        pass

    def trainChar(self, char, img_arr):
        for img in img_arr:
            resized = cv2.resize(img, (32, 32), interpolation=cv2.INTER_AREA)

            imgvector = self.generateRowVector(resized)  # Use own implementation
            self.matrix.append(imgvector)

    def testChar(self, char, img):
        resized = cv2.resize(img, (32, 32), interpolation=cv2.INTER_AREA)
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
        dimensions = 6
        # DO NOT TOUCH THIS!! This switches our column-first data to line-first data, as expected by numpy
        matrix = np.array(self.matrix).T

        q = 1.0 / matrix.shape[1] * np.cov(matrix.T, rowvar=False) - np.matmul(np.mean(matrix, 0), np.mean(matrix, 0).T)

        ew, ev = eigs(q, k=dimensions)

        return np.matmul(ev.T, matrix)
