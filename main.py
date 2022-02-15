import cv2
import numpy as np
import matplotlib.pyplot as mpl

#ALGO:
#1 IF IT'S UNPAINTED = PAINT IT
#2 IF IT'S PAINTED = PAINT THE NEXT UNPAINTED PIXEL
#  AND CLEAR ALL PIXELS ON THE LEFT TO IT

Widght, Height = 100, 100

Img = np.zeros( (Widght, Height, 3), np.uint8 )
Img[:,:] = (255,255,255)

print(Img[10,10])

Cpixx = 0 #current pixel coordinate x (stands for Current PIXel X)
Cpixy = 0 #current pixel coordinate y
Black = False #if all pixels are black?
WhitePixel = np.array([255,255,255])

while Black == False:
    #step 1
    if np.array_equal(Img[Cpixx, Cpixy], WhitePixel) == True:
        Img[Cpixx, Cpixy] = (0,0,0)

    #step 2
    #if

    if Cpixx < Widght:
        Cpixx = Cpixx + 1
    if Cpixx == Widght and Cpixy < Height:
        Cpixy = Cpixy + 1
        Cpixx = 0
        if Cpixy == Height and Cpixx == 0:
            Black = True

    cv2.imshow('image', Img)
    cv2.waitKey(1)
