# -*- coding: utf-8 -*-
"""
02200201081-AYŞE DEVEDEN
""" 

import cv2
import numpy as np
import matplotlib.pyplot as plt

resim= cv2.imread("baboon.jpg",0)
cv2.imshow("Resim",resim)  

plt.hist(resim.ravel(),256,[0,256])
plt.show()

print(resim)            
print (resim.shape)  

cv2.waitKey(0)           
cv2.destroyAllWindows()  


