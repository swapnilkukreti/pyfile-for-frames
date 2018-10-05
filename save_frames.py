# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 18:34:56 2018

@author: SWAPNIL_KUKRETI
"""




import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('1.MP4')

try:
    if not os.path.exists('1'):
        os.makedirs('1')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    
    name = './1/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)  
    cv2.imwrite(name, frame)

   
    currentFrame += 1
    if not ret:
        break
cap.release()
cv2.destroyAllWindows()



