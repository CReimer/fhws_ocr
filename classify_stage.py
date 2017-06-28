#!/usr/bin/python

import string
import cv2
import numpy

from classes.preprocessing import Preprocessing
from classes.tools import Tools
from classes.database import Database
from classes.histogram import Histogram
from classes.featureExtraction import FeatureExtraction
from classes.pca import PCA

tools = Tools()
database = Database()
database.loadDatabase()

## CLASSIFICATION
featureVectors = database.readFeatureVectors()
for char in featureVectors:
    for char_vector_count in featureVectors[char]:
        membershipvalue = 0  # Example value
        database.add("featureMembership", char + str(char_vector_count),
                     membershipvalue)  # Write to database. Don't forget to save database with database.saveDatabase()

        membershipvalue = database.read("featureMembership", char + str(char_vector_count))  # Read back from database.

# Testbild wird hier geladen und auf gleiche Weise durch Preprocessing gejagt
img = cv2.imread('trainingdata/Serif.png', cv2.IMREAD_GRAYSCALE)
preprocess = Preprocessing(img)
preprocess.binariseImg()
splitted_chars = preprocess.splitChars()
# Hier sollte ein Array mit nur einem Element (nur ein Buchstabe) erreicht sein.

# Histogram
histogram2 = Histogram(splitted_chars[0])
histogram2.row_histogram()
histogram_merkmale = histogram2.line_histogram()

# Pixel Average
pix_av2 = FeatureExtraction(splitted_chars[0])
pix_av_merkmale = pix_av2.getpixelaverage()

# PCA
pca2 = PCA()
pca2.testChar(splitted_chars[0])  # In PCA Klasse laden

pca2.matrix -= numpy.array(database.read('common', 'pca_mean'))  # Mean Vector aus Datenbank
pca_merkmale = pca2.pca(
    numpy.array(database.read('common',
                              'pca_eig')[0]))
