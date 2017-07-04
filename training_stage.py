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
from classes.pca import PCA

tools = Tools()
database = Database()
database.initializeEmpty()

char_values = string.ascii_uppercase + string.ascii_lowercase  # Expected characters in Trainings Set

splitted_t_set = []

for t_set in glob.glob('./trainingdata/*.png'):
    print("Reading image: " + t_set)
    img = cv2.imread(t_set, cv2.IMREAD_GRAYSCALE)
    preprocess = Preprocessing(img)
    preprocess.binariseImg()
    splitted_chars = preprocess.splitChars()
    splitted_t_set.append(splitted_chars)

# Histogram
for i in range(len(char_values)):
    for font in splitted_t_set:
        histogram = Histogram(font[i])
        database.add(char_values[i], 'histogram', histogram.rowWert2wert())# [histogram.line_histogram(), histogram.row_histogram()])

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
database.add('common', 'pca_mean', list(mean_vector))
pca.matrix -= mean_vector

# Merkmale für alle Buchstaben in Reihenfolge wie in char_values
eigenvector = pca.generate_eigenvector()

database_eig = []
for i in eigenvector:
    temp = []
    for j in i:
        temp.append(float(j))
    database_eig.append(temp)

database.add('common', 'pca_eig', database_eig)
pca_merkmale = pca.pca(eigenvector)
for i in range(len(pca_merkmale.T)):
    temp = list()
    for j in list(pca_merkmale.T[i]):
        temp.append(float(j))

    database.add(char_values[math.floor(i / len(splitted_t_set))], 'pca', temp)

# Datenbank speichern
database.saveDatabase()
