import cv2
import numpy as np
import matplotlib.pyplot as mpl

#ALGO:
#1 IF IT'S UNPAINTED = PAINT IT
#2 IF IT'S PAINTED = PAINT THE NEXT UNPAINTED PIXEL
#  AND CLEAR ALL PIXELS ON THE LEFT TO IT

Widght, Height = 100, 100

Img = np.zeros( (Widght, Height, 3), np.uint8 )
#Widght, Height = Widght-1, Height-1 #because the counting starts from 0
Img[:,:] = (255,255,255)

print(Img[10,10])

Cpixx = 0 #current pixel coordinate x (stands for Current PIXel X)
Cpixy = 0 #current pixel coordinate y
Black = False #if all pixels are black?
WhitePixel = np.array([255,255,255])

while Black == False:
    for Cpixx in range(0, Widght):
        for Cpixy in range(0, Height):
            print(Cpixx, Cpixy)
            if np.array_equal(Img[Cpixx, Cpixy], WhitePixel) == True:
                Img[Cpixx, Cpixy] = (0,0,0)
                for Cpixx in range(Cpixx, -1, -1):
                    for Cpixy in range(Cpixy, -1, -1):
                        Img[Cpixx, Cpixy] = (0,0,0)
                        print("a")
            if Cpixx == Widght - 1 and Cpixy == Height - 1:
                Black = True

    #cv2.imshow('image', Img)
    #cv2.waitKey(0)
