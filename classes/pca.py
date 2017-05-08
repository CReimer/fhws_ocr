import numpy
import cv2
#from matplotlib.mlab import PCA as matplot_pca
from classes.database import Database

#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D


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

    def trainCharOcv(self, char, img_arr):
        matrix2 = []
        # matrix = []  # Will be multidimensional -> [rows][lines]
        for img in img_arr:
            imgvector = img.flatten()  # array to vector
            try:
                matrix2 = numpy.vstack((matrix2, imgvector))  # append vertically to matrix
            except:
                matrix2 = imgvector  # No matrix? Well our vector starts the new matrix

        self.CvPca(matrix2)

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

    def CvPca(self, matrix):
        mean, eigenvectors = cv2.PCACompute(matrix, mean=numpy.array([]))
        print(mean)
        print(eigenvectors)

    @staticmethod
    def mlabPCA(matrix):
        # mlab's PCA expects a 2d numpy Array
        myData = numpy.array(matrix)
        myData = myData.T  # We have to transpose the matrix here. Matplot expects [line][row] and we have [row][line]
        results = matplot_pca(myData)

        # this will return an array of variance percentages for each component
        # return results.fracs

        # this will return a 2d array of the data projected into PCA space
        return results

    @staticmethod
    def plotPCA(result):
        x = []
        y = []
        z = []
        for item in result.Y:
            x.append(item[0])
            y.append(item[1])
            z.append(item[2])

        plt.close('all')  # close all latent plotting windows
        fig1 = plt.figure()  # Make a plotting figure
        ax = Axes3D(fig1)  # use the plotting figure to create a Axis3D object.
        pltData = [x, y, z]
        ax.scatter(pltData[0], pltData[1], pltData[2], 'bo')  # make a scatter plot of blue dots from the data

        # make simple, bare axis lines through space:
        xAxisLine = ((min(pltData[0]), max(pltData[0])), (0, 0),
                     (0, 0))  # 2 points make the x-axis line at the data extrema along x-axis
        ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'r')  # make a red line for the x-axis.
        yAxisLine = ((0, 0), (min(pltData[1]), max(pltData[1])),
                     (0, 0))  # 2 points make the y-axis line at the data extrema along y-axis
        ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'r')  # make a red line for the y-axis.
        zAxisLine = ((0, 0), (0, 0), (
            min(pltData[2]), max(pltData[2])))  # 2 points make the z-axis line at the data extrema along z-axis
        ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'r')  # make a red line for the z-axis.

        # label the axes
        ax.set_xlabel("x-axis label")
        ax.set_ylabel("y-axis label")
        ax.set_zlabel("y-axis label")
        ax.set_title("The title of the plot")
        plt.show()  # show the plot
