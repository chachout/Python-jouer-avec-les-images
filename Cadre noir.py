from PIL import Image
import numpy as np
import os as os
import matplotlib.pyplot as plt
import matplotlib.image as im
os.chdir('C:\\Users\\pierre\\Desktop')
img=Image.open("IMAG0449_andyW.jpg")
tab=np.array(img)
print(tab)
print(tab.shape)
for k in range(0,3):    
    for i in range(0,5856):
        for z in range (7675,7775):
            tab[i][z][k]=0
            z=z+1
        for m in range(0,100):
            tab[i][m][k]=0
            m=m+1
        i=i+1
    for j in range (0,7776):
        for n in range (5755,5855):
            tab[n][j][k]=0
            n=n+1
        for o in range (0,100):
            tab[o][j][k]=0
            o=o+1
        j=j+1
    k=k+1
nouvelle_image=Image.fromarray(tab)
nouvelle_image.show()
nouvelle_image.save("IMAG0449_cadrenoir.jpg")