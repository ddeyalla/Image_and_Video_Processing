# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 01:21:29 2019

@author: Divyanshu Deyalla
"""

import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("outme.avi", fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV) 
    cv2.imshow("yuv", gray)
    cv2.imshow("frame", frame)
    out.write(gray)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

