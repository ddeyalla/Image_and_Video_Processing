# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 00:26:32 2019

@author: Divyanshu Deyalla
"""

import cv2
import numpy as np

cameraCapture = cv2.VideoCapture(0) #video capture intial setup
fourcc = cv2.VideoWriter_fourcc(*"XVID") #codec
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480)) #output parameters

#return value and frame
while True:
    ret, frame = cameraCapture.read() # read frame
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #gray scale screen
    out.write(frame) #write frame
    cv2.imshow("frame", frame) #show frame 
    cv2.imshow("Gray", gray) #show gray
    
    if cv2.waitKey(1) & 0xFF == ord("q"): #to stop the infinite loop
        break
    
cameraCapture.release() #release capture
out.release() #release output
cv2.destroyAllWindows()