from PIL import Image
import numpy as np
import os as os
import matplotlib.pyplot as plt
import matplotlib.image as im
os.chdir('C:\\Users\\pierre\\Desktop')
img=Image.open("IMAG0449.jpg")
tab=np.array(img)
"""img.show() 
print(tab)
print(tab.shape)"""
for i in range(0,1952):
    for j in range(0,2592):
        tab[i][j][0]=0
        tab[i][j][1]=0
        tab[i][j][2]=0
        
        j=j+1
    i=i+1


nouvelle_image=Image.fromarray(tab)
nouvelle_image.show()
nouvelle_image.save("IMAG0449_noir.jpg")