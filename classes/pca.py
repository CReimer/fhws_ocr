import numpy
import cv2


class PCA:
    def __init__(self):
        self.matrix = []
        pass

    def trainChar(self, char, img_arr):
        for img in img_arr:
            # imgvector = img.flatten()  # array to vector
            imgvector = self.generateRowVector(img)  # Use own implementation
            self.matrix.append(imgvector)
            # self.matrix = numpy.vstack((self.matrix, imgvector))  # append vertically to matrix

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

    def fixedVectorLength(self):
        maxLength = 0
        for i in self.matrix:
            if len(i) > maxLength:
                maxLength = len(i)

        for i in range(len(self.matrix)):
            temp = [numpy.uint8(0)] * maxLength
            for j in range(maxLength):
                try:
                    temp[j] = self.matrix[i][j]
                except IndexError:
                    break
            self.matrix[i] = temp

        print("Length: " + str(maxLength))

    def pca(self):
        matrix = numpy.array(self.matrix)
        # matrix = numpy.transpose(matrix)

        cov = numpy.dot(matrix, matrix.T)
        eigvals, eigvecs = numpy.linalg.eig(cov)

        eig_pairs = [(numpy.abs(eigvals[i]), eigvecs[:, i]) for i in range(len(eigvals))]
        eig_pairs.sort(key=lambda x: x[0], reverse=True)

        for i in range(len(eig_pairs)):
            if eig_pairs[i][0] > 1:
                print(str(i) + ' ' + str(eig_pairs[i][0]))


