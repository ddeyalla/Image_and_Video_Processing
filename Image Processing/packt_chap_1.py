# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:24:13 2019

@author: Divyanshu Deyalla
"""

import numpy as np
import cv2
img = cv2.imread("C:/Users/Divyanshu Deyalla/Desktop/Image Processing/Mona-Lisa-256x256.jpg", cv2.IMREAD_GRAYSCALE)

print("original image shape : ", img.shape) #printing image shape

width, height = 128, 256

resized_img = cv2.resize(img, (width, height))
print("resized image shape : ", resized_img.shape) 

w_mul, h_mul = 0.25, 0.5
resized_img_mul = cv2.resize(img, (0,0), resized_img, w_mul, h_mul)
print("image shape : ", resized_img_mul)

img_flip = cv2.flip(img, -1)

cv2.imshow("image", img_flip)
cv2.imwrite("flipped.png", img_flip, [cv2.IMWRITE_PNG_COMPRESSION, 0])
saved_img = cv2.imread("C:/Users/Divyanshu Deyalla/Desktop/Image Processing/flipped.png", cv2.IMREAD_ANYCOLOR)
assert saved_img.all() == img.all()
cv2.waitKey(0)
cv2.destroyAllWindows()
