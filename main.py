#!/usr/bin/python
import string

import cv2
import numpy
import numpy as np
import math

from classes.preprocessing import Preprocessing
from classes.tools import Tools
from classes.database import Database
from classes.pca import PCA
from classes.peak import Peak
from scipy import linalg as LA

tools = Tools()
database = Database()
# database.initializeEmpty()

# database.loadDatabase()
# database.add('a', 'histogram' "asdfg")
# database.saveDatabase()
#
# exit()

# img = cv2.imread('1_pontifically_58805.jpg', cv2.IMREAD_GRAYSCALE)


img = cv2.imread('trainingdata/Sans.png', cv2.IMREAD_GRAYSCALE)
preprocess = Preprocessing(img)
preprocess.binariseImg()
# preprocess.skelettizeImg()
sans_chars = preprocess.splitChars()

img = cv2.imread('trainingdata/Serif.png', cv2.IMREAD_GRAYSCALE)
preprocess = Preprocessing(img)
preprocess.binariseImg()
# preprocess.skelettizeImg()
serif_chars = preprocess.splitChars()

# for i in serif_chars:
#     if i is not None:
#         tools.showImage(i)
# tools.showImage(serif_chars[0])
# tools.writeImage(serif_chars[0], 'out1.jpg')


# preprocess2 = Preprocessing(serif_chars[0])
# preprocess2.binariseImg()
# preprocess2.skelettizeImg()
# tools.writeImage(preprocess2.img, 'out2.jpg')
#
# img3 = cv2.imread('Unbenannt.png', cv2.IMREAD_GRAYSCALE)
# preprocess2 = Preprocessing(img3)
# preprocess2.binariseImg()
# preprocess2.skelettizeImg()
# tools.writeImage(preprocess2.img, 'out3.jpg')


char_values = string.ascii_uppercase + string.ascii_lowercase

pca = PCA()
# peak = Peak()

for i in range(len(char_values)):
    pca.trainChar(char_values[i], [serif_chars[i], sans_chars[i]])
    # peak.trainChar(char_values[i], [serif_chars[i], sans_chars[i]])

mean_vector = numpy.mean(pca.matrix, 0)  # MERKEN!!
database.add('', 'pca_mean', list(mean_vector))
pca.matrix -= mean_vector

# Merkmale für alle Buchstaben in Reihenfolge wie in char_values
pca_merkmale = pca.pca()
for i in range(len(pca_merkmale.T)):
    temp = list()
    for j in list(pca_merkmale.T[i]):
        temp.append(float(j))

    database.add(char_values[math.floor(i / 2)], 'pca', temp)
database.saveDatabase()

char_values = 'A'
pca2 = PCA()

for i in range(len(char_values)):
    pca2.testChar(char_values[i], serif_chars[i])
    pca2.testChar(char_values[i], serif_chars[i])  # Zweimal als Workaround für Eigenwertanalyse

pca2.matrix -= mean_vector

# Merkmale für alle Buchstaben in Reihenfolge wie in char_values. Einzelne Buchstaben funktioniert nicht. Rücksprache mit Fetzer nötig.
pca2_merkmale = pca2.pca()

exit()

#
# preprocess.binariseImg()
# img = preprocess.img
# tools.showImage(img, "Before")

# preprocess.skelettizeImg()
# tools.showImage(preprocess.img)
# tools.writeImage(preprocess.img, "test.png")

# for idx in range(len(chars)):
#     tools.writeImage(chars[idx], "single" + str(idx) + '.jpg')
