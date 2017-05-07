import numpy
from matplotlib.mlab import PCA

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


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

# __Flo's Part___

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

    def plotPCA(self, result):
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
