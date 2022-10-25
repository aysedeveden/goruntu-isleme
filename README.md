"""
02200201081-AYŞE DEVEDEN
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

h='height'
w='width'
c='channel'
u,v,I=(0,0,0)
print(u,v,I)


resim= cv2.imread("baboon.jpg",0)
cv2.imshow("Resim",resim)
  


Hist = np.zeros(256)


h,w,c=resim.shape
(h, w) = resim.shape[:2]
for v in range (0, u<h):
   for u in range (0, u<w):
        i= I(u,v)
        Hist[i]=Hist[i]+1 
          

plt.hist(resim) #histogram çizdirme
plt.show()



print(resim)             #matrisleri gösterir
print (resim.shape)  

cv2.waitKey(0)           
cv2.destroyAllWindows()  


