'''
Perform morphological operations
1. Dilation
2. Erosion
'''

import cv2
import numpy as np

img = cv2.imread('j.png',0)
rows,col = img.shape
#### CONVERTING TO BINARY ###############
for i in range(0,rows):
    for j in range(0,col):
        if (img[i,j]>=128):
            img[i,j] = 255
        else:
            img[i,j] = 0
#cv2.imshow('img',img)
#cv2.waitKey(0)
###### EROSION ################
erode = img
cv2.imwrite('ini_erode.png',erode)
for i in range(1,rows-1):
    for j in range(1,col-1):
        if(img[i,j+1]==0 or img[i+1,j]==0 or img[i,j-1]==0 or img[i-1,j]==0):
            erode[i,j] = 0
cv2.imwrite('eroded_img.png',erode)
###### DILATION ###############

dilate = img
for i in range(1,rows-1):
    for j in range(1,col-1):
        if(img[i,j+1]==255 or img[i+1,j]==255 or img[i,j-1]==255 or img[i-1,j]==255):
            dilate[i,j] = 255
cv2.imwrite('dilated_img.png',dilate)

