"""
02200201081-AYŞE DEVEDEN
"""

import cv2

import numpy as np

import matplotlib.pyplot as plt




resim= cv2.imread("baboon.jpg",0)

cv2.imshow("Resim",resim)
  

hist,bins = np.histogram(resim.flatten(),256,[0,256])

cdf = hist.cumsum()

cdf_normalized = cdf * hist.max()/ cdf.max()

plt.hist(resim) #histogram çizdirme

plt.show()



print(resim)             #matrisleri gösterir

print (resim.shape)  

cv2.waitKey(0)           

cv2.destroyAllWindows()  



