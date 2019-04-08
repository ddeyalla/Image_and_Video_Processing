# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 01:27:16 2019

@author: Divyanshu Deyalla
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #hue sat value
    lower_blue = np.array([110,110,110]) #creating a red upper and lower value/ entire range of the cap
    upper_blue = np.array([255,255,255])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue) # creating a mask for the video with the red ranges
    res = cv2.bitwise_and(frame, frame, mask = mask) # where, frame, mask
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()