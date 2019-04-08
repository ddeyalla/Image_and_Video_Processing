# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:38:20 2019

@author: Divyanshu Deyalla
"""
#import
import numpy as np
import cv2
img_a = cv2.imread("C:/Users/Divyanshu Deyalla/Desktop/Image Processing/a.png", cv2.IMREAD_COLOR)
img_b = cv2.imread("C:/Users/Divyanshu Deyalla/Desktop/Image Processing/b.png", cv2.IMREAD_COLOR)
img_c = cv2.imread("C:/Users/Divyanshu Deyalla/Desktop/Image Processing/c.png", cv2.IMREAD_COLOR)

#------------------------------------------------------------------------------ arithematic operations on image
#add = cv2.add(img_a, img_b) #adding image / adding each pixel
#sub = cv2.subtract(img_a, img_b) #subtracting image 
#mul = cv2.multiply(img_a, img_b) #multiply image

#------------------------------------------------------------------------------ weighted image /  opaqueness is not affected
#weigthed_add = cv2.addWeighted(img_a, 0.6, img_b, 0.4, 0)

#------------------------------------------------------------------------------ logical operations
rows,cols,channels = img_c.shape #getting the shape of the image to be layered

roi = img_a[0:rows, 0:cols] #selecting the region of image 1

image2gray = cv2.cvtColor(img_c, cv2.COLOR_BGR2GRAY) #CONVERT the 2nd image to be layered TO GRAYSCALE

ret, mask = cv2.threshold(image2gray, 220, 255, cv2.THRESH_BINARY_INV) #image, minimum threshold, maximum threshold, binary threshold #making a mask from the thresholded image

mask_inv = cv2.bitwise_not(mask) #invert the mask / all the black values region will be removed #invisble part 

img_a_bg = cv2.bitwise_and(roi, roi, mask = mask_inv) #image c background reference the blacked out area

img_c_fg = cv2.bitwise_and(img_c, img_c, mask = mask) #image c only the masked area will be visible

dst = cv2.add(img_a_bg, img_c_fg) #adding the background of image a to image c

img_a[0:rows, 0:cols] = dst #imposing the aoi
 
#------------------------------------------------------------------------------ output weigthed image
#cv2.imshow("weighted add", weigthed_add)

#------------------------------------------------------------------------------ output logical image
cv2.imshow("rest", img_a) #final output
#cv2.imshow("mask_inv", mask_inv)
#cv2.imshow("mask", mask)
#cv2.imshow("image_a bg", img_a_bg)
#cv2.imshow("image_c fg", img_c_fg)

#------------------------------------------------------------------------------ show original image
#cv2.imshow("Image a", img_a)
#cv2.imshow("Image b", img_b)

#------------------------------------------------------------------------------ show arithematic operations
#cv2.imshow("Image add", add)
#cv2.imshow("Image sub", sub)
#cv2.imshow("Image mul", mul)

#------------------------------------------------------------------------------ save
#cv2.imwrite("add.png", add)
#cv2.imwrite("sub.png", sub)
#cv2.imwrite("mul.png", mul)
cv2.waitKey(0)
cv2.destroyAllWindows()