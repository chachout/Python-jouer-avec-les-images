import numpy as np
import os as os
import matplotlib.pyplot as qt
import matplotlib.image as im
os.chdir("C:/Users/pierre/Desktop")
imnb = im.imread('IMAG0449.jpg')
qt.imshow(imnb) 
qt.colorbar()
imnb.set_cmap('gray')
qt.figure ()
im2=im.imread('IMAG0372.jpg')+imnb
imp2=qt.imshow(im2)
imp2.set_cmap('gray')
im.insave('IMAG03.jpg',im2,cmap='gray')

print(im2)
print(im2.shape)
