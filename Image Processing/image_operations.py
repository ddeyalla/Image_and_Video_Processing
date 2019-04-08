# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:11:55 2019

@author: Divyanshu Deyalla
"""
import numpy as np
import cv2
img = cv2.imread("C:/Users/Divyanshu Deyalla/Desktop/Image Processing/Mona-Lisa-256x256.jpg", cv2.IMREAD_COLOR)

px = img[55,55] #pixel co ordinates
img[55,55] = [255, 255, 255] #setting pixel color
print(px) #printing pixel

#REGION OF IMAGE (ROI) - Specify region of imag
roi = img[100:155, 100:155] = [255, 255, 255] #region of the image we are filling with white pixels

mona = img[37:111, 107:194] #selecting a region of image we want to copy
img[0:74, 0:87] = mona #on the region we are replacing it from above

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
