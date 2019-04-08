# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:25:53 2019

@author: Divyanshu Deyalla
"""

import numpy as np
import cv2

cv2.namedWindow("Window")

fill_value = np.array([255,255,255], np.uint8)

def trackbar(idx, value):
    fill_value[idx] = value
    
cv2.createTrackbar("R", "Window", 255, 255, lambda v : trackbar(2,v))
cv2.createTrackbar("G", "Window", 255, 255, lambda v : trackbar(1,v))
cv2.createTrackbar("B", "Window", 255, 255, lambda v : trackbar(0,v))

while True:
    image = np.full((500,500,3), fill_value)
    cv2.imshow("Window", image)
    key = cv2.waitKey()
    if key == 27:
        break
cv2.destroyAllWindows()