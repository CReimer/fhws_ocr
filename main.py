#!/usr/bin/python
import string

import cv2
from classes.preprocessing import Preprocessing
from classes.tools import Tools
from classes.database import Database
from classes.pca import PCA

tools = Tools()
# database = Database()
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


char_values = string.ascii_uppercase + string.ascii_lowercase
for i in range(len(char_values)):
    pca = PCA()
    pca.trainCharOcv(char_values[i], [sans_chars[i], sans_chars[i]])

exit()

# tools.showImage(chars[2])
# preprocess.binariseImg()
# img = preprocess.img
# tools.showImage(img, "Before")

# chars = preprocess.splitChars()
# preprocess.skelettizeImg()
# tools.showImage(preprocess.img)
# tools.writeImage(preprocess.img, "test.png")

for idx in range(len(chars)):
    tools.writeImage(chars[idx], "single" + str(idx) + '.jpg')
