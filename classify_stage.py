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
from classes.classify import Classify

tools = Tools()
database = Database()
database.loadDatabase()

def run(singleChar):
    # Histogram
    histogram2 = Histogram(singleChar)
    histogram_merkmale = histogram2.rowWert2wert()      # line_histogram() + histogram2.row_histogram()

    # Pixel Average
    pix_av2 = FeatureExtraction(singleChar)
    pix_av_merkmale = pix_av2.getpixelaverage()

    # PCA
    pca2 = PCA()
    pca2.testChar(singleChar)  # In PCA Klasse laden

    pca2.matrix -= numpy.array(database.read('common', 'pca_mean'))  # Mean Vector aus Datenbank
    pca_merkmale = pca2.pca(
        numpy.array(database.read('common',
                                  'pca_eig')[0]))
    temp = list()
    for j in list(pca_merkmale.T[0]):
        temp.append(float(j))

    featureVector = [pix_av_merkmale] + histogram_merkmale + temp
    classify = Classify()
    classify.crispKnn(featureVector, 3)
    print(featureVector)

characterCount = 4
## CLASSIFICATION
featureVectors = database.readFeatureVectors()
for char in featureVectors:
    for char_vector_count in featureVectors[char]:
        membershipvalue = 0  # Example value
        database.add("featureMembership", char + str(char_vector_count),
                     membershipvalue)  # Write to database. Don't forget to save database with database.saveDatabase()

        membershipvalue = database.read("featureMembership", char + str(char_vector_count))  # Read back from database.

# Testbild wird hier geladen und auf gleiche Weise durch Preprocessing gejagt
img = cv2.imread('trainingdata/trainingsdata.off/helloworld.png', cv2.IMREAD_GRAYSCALE)
preprocess = Preprocessing(img)
preprocess.binariseImg()
splitted_chars = preprocess.splitChars()

for singleChar in splitted_chars:
    run(singleChar)