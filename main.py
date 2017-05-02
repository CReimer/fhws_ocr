#!/usr/bin/python

import cv2
from classes.histogram import Histogram
from classes.preprocessing import Preprocessing
from classes.tools import Tools

img = cv2.imread('25_CAPSIZES_11382.jpg', cv2.IMREAD_GRAYSCALE)

test = Preprocessing(img)
tools = Tools()


test.binariseImg()
testJ = Histogram(test.img)
f = testJ.runterfallen()
for idx in range(len(f)):
    print(f[idx])

print("_______________________________________________________________________________________________")

f = testJ.zurseiterutschen()
for idx in range(len(f)):
   print(f[idx])

tools.showImage(test.img)
chars = test.splitChars()

for idx in range(len(chars)):
    tools.writeImage(chars[idx], "single" + str(idx) + '.jpg')



