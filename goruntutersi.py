# -*- coding: utf-8 -*-
"""
02200201081-AYŞE DEVEDEN
""" 


import cv2
import numpy as np
import matplotlib.pyplot as plt


resim= cv2.imread("kalp.jpg")
cv2.imshow("Resim",resim)

[h,w]=resim.shape
new_resim = np.zeros([h,w])
for i in  range.items(h):
    for j in range.items(w):
        new_resim[i,j] = 255 - resim[i,j]

print(new_resim[i,j])            
cv2.imshow("Negatif Resim",new_resim)

cv2.waitKey(0)           
cv2.destroyAllWindows()  