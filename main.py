#!/usr/bin/python

import cv2
from classes.preprocessing import Preprocessing
from classes.tools import Tools
from classes.featureExtraction import FeatureExtraction

img = cv2.imread('1_pontifically_58805.jpg', cv2.IMREAD_GRAYSCALE)

test = Preprocessing(img)
tools = Tools()

test.stretchContrast()
#tools.showImage(test.img)
test.binariseImg()

test_flo = FeatureExtraction(test.img)
test_flo.getpixelaverage()


tools.showImage(test.img)
chars = test.splitChars()

for idx in range(len(chars)):
    tools.writeImage(chars[idx], "single" + str(idx) + '.jpg')
