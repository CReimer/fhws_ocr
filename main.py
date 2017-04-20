#!/usr/bin/python

import cv2
from classes.preprocessing import Preprocessing

img = cv2.imread('1_pontifically_58805.jpg', cv2.IMREAD_GRAYSCALE)

test = Preprocessing(img)
test.binariseImg()
# test.showImage()
test.splitChars()
# test.showImage()

