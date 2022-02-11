import cv2
import numpy as np
import matplotlib.pyplot as mpl

#ALGO:
#1 IF IT'S UNPAINTED = PAINT IT
#2 IF IT'S PAINTED = PAINT THE NEXT UNPAINTED PIXEL
#  AND CLEEAR ALL PIXELS ON THE LEFT TO IT

img = np.zeros( (100,100,3), np.uint8 )
img[:,:] = (255,255,255)

print(img)

cpixx = 0 #current pixel coordinate x
cpixy = 0 #current pixel coordinate y
black = false #if all pixels are black?

while black == false
    img[cpixx,pixy] = (0,0,0)
    if ()

    cv2.imshow('image',img)
    cv2.waitKey(0)
