# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:30:06 2019

@author: Divyanshu Deyalla
"""

#thresholding either 0 or 1. black or white
#apply threshold as binary on image
#grayscale the image
#apply gaussian adaptive threshold
#The thresholding algorithms can be categorized into six classes: 
#      histogram shape-based methods
#      clustering-based methods
#      entropy based methods
#      object attribute-based methods
#      the spatial methods
#      local methods based on the local characteristics of each pixel
#Otsu’s thresholding technique is a classification-based method which searches for the the threshold that minimizes the
#   intra-class variance, defined as a weighted
#   sum of variances of the two classes
#

import numpy as np
import cv2
img = cv2.imread("C:/Users/Divyanshu Deyalla/Desktop/Image Processing/thresh.jpg", cv2.IMREAD_COLOR)
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY) #image, min threshold value, max threshold vlaue, binary threshold
graysacled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(graysacled, 12, 255, cv2.THRESH_BINARY)
retval3, otsu = cv2.threshold(graysacled, 25, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#Gaussian adaptive threshold
gauss = cv2.adaptiveThreshold(graysacled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


#cv2.imshow("original image", img)
#cv2.imshow("Thresh image", threshold)
#cv2.imshow("Thresh Gray image", threshold2)
cv2.imshow("Gauss", gauss)
cv2.imshow("otsu", otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()