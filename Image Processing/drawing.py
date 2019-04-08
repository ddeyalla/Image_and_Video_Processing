# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:50:14 2019

@author: Divyanshu Deyalla
"""
import cv2
import numpy as np

img = cv2.imread("C:/Users/Divyanshu Deyalla/Desktop/Image Processing/Mona-Lisa-256x256.jpg", 0)
cv2.line(img, (0, 0), (150, 150), (0,255,0), 5) #image, start, end, color, line width
cv2.rectangle(img, (15, 25), (200,150), (0,0,250), 5) #image, start end, bottom end, color , thickness
cv2.circle(img, (100, 63), 55, (0,0,0), -1)#image, position, radius, color , thickness

pts = np.array([[10, 5], [20, 30], [70, 25], [50, 10], [50, 10]], np.int32)
#pts = pts.reshape((-1, 1, 2)) 
cv2.polylines(img, [pts], True, (0,0,0), 5 )#image, points, connect, color, thickness 

font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img, "OpenCV", (0, 130), font, 1, (0,45,0), 2, cv2.LINE_AA) #image, text, position, font, scale, color, size, anti aliasing

cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()