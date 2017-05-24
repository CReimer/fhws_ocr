import numpy
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
        dimensions = 3
        # mean_vector = numpy.array(mean_vector)
        matrix = numpy.array(self.matrix)
        # a = 1.0 / matrix.shape[0]
        b = numpy.cov(matrix, rowvar=False)
        # c = numpy.mean(matrix.T, 0) * numpy.mean(matrix, 1)

        evals, evecs = eigsh(b)

        idx = numpy.argsort(evals)[::-1]
        evecs = evecs[:, idx]
        evals = evals[idx]

        evecs = evecs[:, :dimensions]

        merkmale = numpy.dot(evecs.T, matrix.T).T

        print(merkmale[0])
        print(merkmale[1])

        # q = a * b - c

        # ew, ev = numpy.linalg.eig(kernel_matrix)

        # ew, ev = eigs(q, k=4)

        # eig_val_cov = ew
        # eig_vec_cov = ev
        # merkmale = ev.T * matrix

        # eig_pairs = [(numpy.abs(eig_val_cov[i]), eig_vec_cov[:, i]) for i in range(len(eig_val_cov))]
        # eig_pairs.sort(key=lambda x: x[0], reverse=True)

        # print(eig_pairs[0][1][0])
        # print(eig_pairs[1][1][0])
        # print(eig_pairs[2][1][0])
