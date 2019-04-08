# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 00:14:49 2019

@author: Divyanshu Deyalla
"""

import cv2
import numpy as np
import os

randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)

grayImg = flatNumpyArray.reshape(300, 400)
cv2.imwrite("C:/Users/Divyanshu Deyalla/Desktop/Image Processing/rand.png", grayImg)

bgrImg = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite("C:/Users/Divyanshu Deyalla/Desktop/Image Processing/bgr.png", bgrImg)