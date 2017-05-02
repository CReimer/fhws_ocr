#!/usr/bin/python

import cv2
from classes.preprocessing import Preprocessing
from classes.tools import Tools

img = cv2.imread('25_CAPSIZES_11382.jpg', cv2.IMREAD_GRAYSCALE)

test = Preprocessing(img)
tools = Tools()


test.binariseImg()
tools.showImage(test.img)
chars = test.splitChars()

for idx in range(len(chars)):
    tools.writeImage(chars[idx], "single" + str(idx) + '.jpg')



