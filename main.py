#!/usr/bin/python
import string

import cv2
import numpy
import math
import glob

from classes.preprocessing import Preprocessing
from classes.tools import Tools
from classes.database import Database
from classes.histogram import Histogram
from classes.featureExtraction import FeatureExtraction
from classes.sternmuster import Sternmuster
from classes.pca import PCA

tools = Tools()
database = Database()
database.initializeEmpty()

# database.loadDatabase()

char_values = string.ascii_uppercase + string.ascii_lowercase # Expected characters in Trainings Set

splitted_t_set = []

for t_set in glob.glob('./trainingdata/*.png'):
    print("Reading image: " + t_set)
    img = cv2.imread('trainingdata/Sans.png', cv2.IMREAD_GRAYSCALE)
    preprocess = Preprocessing(img)
    preprocess.binariseImg()
    splitted_chars = preprocess.splitChars()
    splitted_t_set.append(splitted_chars)

# Histogram
for i in range(len(char_values)):
    for font in splitted_t_set:
        histogram = Histogram(font[i])
        database.add(char_values[i], 'histogram', [histogram.line_histogram(), histogram.row_histogram()])

# Pixel Average
for i in range(len(char_values)):
    for font in splitted_t_set:
        pix_av = FeatureExtraction(font[i])
        database.add(char_values[i], 'pixelAv', pix_av.getpixelaverage())

# PCA
pca = PCA()

for i in range(len(char_values)):
    temp = []
    for j in splitted_t_set:
        temp.append(j[i])
    pca.trainChar(char_values[i], temp)

mean_vector = numpy.mean(pca.matrix, 0)
database.add('', 'pca_mean', list(mean_vector))
pca.matrix -= mean_vector

# Merkmale für alle Buchstaben in Reihenfolge wie in char_values
eigenvector = pca.generate_eigenvector()
pca_merkmale = pca.pca(eigenvector)
for i in range(len(pca_merkmale.T)):
    temp = list()
    for j in list(pca_merkmale.T[i]):
        temp.append(float(j))

    database.add(char_values[math.floor(i / 2)], 'pca', temp)


# Datenbank speichern
database.saveDatabase()

## CLASSIFICATION


# Testbild wird hier geladen und auf gleiche Weise durch Preprocessing gejagt
img = cv2.imread('test_character.jpg', cv2.IMREAD_GRAYSCALE)
preprocess = Preprocessing(img)
preprocess.binariseImg()
splitted_chars = preprocess.splitChars()  # Hier sollte ein Array mit nur einem Element (nur ein Buchstabe) erreicht sein.


# Histogram
histogram2 = Histogram(img[0])
histogram2.row_histogram()
histogram_merkmale = histogram2.line_histogram()

# Pixel Average
pix_av2 = FeatureExtraction(img[0])
pix_av_merkmale = pix_av2.getpixelaverage()

# PCA
pca2 = PCA()
pca2.testChar(splitted_chars[0])  # In PCA Klasse laden

pca2.matrix -= numpy.array(database.read('', 'pca_mean'))  # Mean Vector aus Datenbank
pca_merkmale = pca2.pca(
    eigenvector)  # Bei einem Buchstaben in char_values ist das hier eine 6x2 Matrix. 6 Zeilen, 2 Spalten. 2 Spalten wegen TODO von oben. Eigenwertanalyse schlägt fehl wenn nur ein Buchstabe getestet wird.

# Merkmale ab hier in histogram_merkmale, pix_av_merkmale und pca_merkmale
