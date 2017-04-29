#!/usr/bin/python

import cv2
from classes.preprocessing import Preprocessing
from classes.tools import Tools

tools = Tools()

img = cv2.imread('1_pontifically_58805.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('Unbenannt.png', cv2.IMREAD_GRAYSCALE)

tools.showImage(img)

preprocess = Preprocessing(img)
preprocess.binariseImg()
img = preprocess.img
tools.showImage(img, "Before")

chars = preprocess.splitChars()
preprocess.skelettizeImg()
tools.showImage(preprocess.img)

for idx in range(len(chars)):
    tools.writeImage(chars[idx], "single" + str(idx) + '.jpg')
