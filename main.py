import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as mpl

#ALGO:
#1 IF IT'S UNPAINTED = PAINT IT
#2 IF IT'S PAINTED = PAINT THE NEXT UNPAINTED PIXEL
#  AND CLEAR ALL PIXELS ON THE LEFT TO IT

Widght, Height = 256, 256

Img = np.zeros( (Widght, Height, 3), np.uint8 )
#Widght, Height = Widght-1, Height-1 #because the counting starts from 0
Img[:,:] = (255,255,255)

#print(Img[10,10])

Cpixx = 0 #current pixel coordinate x (stands for Current PIXel X)
Cpixy = 0 #current pixel coordinate y
Black = False #if all pixels are black?
WhitePixel = np.array([255,255,255])
name = 1

while Black == False:
    while Cpixx < Widght:
        while Cpixy < Height:
            #step 1 and 2
            if np.array_equal(Img[Cpixx, Cpixy], WhitePixel) == True:
                Img[Cpixx, Cpixy] = (0,0,0)
                #clearing
                for Cpixy in range(Cpixy - 1, -1, -1):
                    for Cpixx in range(Cpixx, -1, -1):
                        Img[Cpixx, Cpixy] = (255,255,255)
                #output
                #Im = Image.fromarray(Img)
                #Im.convert("1")
                #Im.save(f"D:\Projects\Image generator\images\{name:04d}.jpeg", 'JPEG')
                #name = name + 1
                cv2.imshow('image', Img)
                cv2.waitKey(1)
            elif Cpixy < Height - 1:
                Cpixy = Cpixy + 1
            else:
                Cpixy = 0
                Cpixx = Cpixx +1
                #check fullness
                if Cpixx == Widght:
                    Black = True
                    Cpixy = Height




    #cv2.imshow('image', Img)
    #cv2.waitKey(0)
