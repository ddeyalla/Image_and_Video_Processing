# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 01:33:37 2019

@author: Divyanshu Deyalla
"""

import cv2 
import numpy as np

img = cv2.imread("C:/Users/Divyanshu Deyalla/Desktop/Image Processing/Mona-Lisa-256x256.jpg", 0)
img2 = np.zeros((512,512,3), np.uint8)
img2 = cv2.rectangle(img2, (384, 263), (45, 70), (0, 255, 0), 3) #(input image , shape, position, color, thickness)
#img3 = cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow("Rect", img2)
cv2.imshow("Image", img)
byteArray = bytearray(img)
grayme = np.array(byteArray).reshape(256,256)

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
 
elif k == ord('s'):
    cv2.imwrite("C:/Users/Divyanshu Deyalla/Desktop/Image Processing/Gray_mona.jpg", img )
    cv2.destroyAllWindows()