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

    def fixedVectorLength(self):
        maxLength = 0
        for i in self.matrix:
            if len(i) > maxLength:
                maxLength = len(i)

        for i in range(len(self.matrix)):
            temp = [0] * maxLength
            for j in range(maxLength):
                try:
                    temp[j] = self.matrix[i][j]
                except IndexError:
                    break
            self.matrix[i] = temp

        print("Length: " + str(maxLength))

    def pca(self):
        matrix = numpy.array(self.matrix)
        mean, eigenvectors = cv2.PCACompute(matrix, mean=numpy.array([]))
        #mean, eigenvectors = cv2.PCACompute(matrix)

        print(eigenvectors)
        # return mean[0][0]
        print(mean)


