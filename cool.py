
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os as os


os.getcwd()
os.chdir("C:/Users/pierre/Desktop")
imgcol=mpimg.imread('IMAG0372.jpg')
plt.imshow(imgcol)
print(imgcol)
print(imgcol.shape)
plt.figure
imgnb=mpimg.imread('IMAG0449.jpg')
imgplot=plt.imshow(imgnb)
print(imgnb)
print(imgnb.shape)
imgplot.set_cmap('cool')
plt.colorbar()

plt.figure()
imgnb2=mpimg.imread('IMAG0372.jpg')+imgnb
imgplot2=plt.imshow(imgnb2)
imgplot2.set_cmap('cool')
plt.colorbar()
mpimg.imsave('IMAG0372.jpg',imgnb2,cmap='cool')