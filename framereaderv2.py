import numpy
import cv2
import sys
import os
import time

# 480x360

curframe = 1
display = ''

while True:
    img = cv2.imread('frame'+str(curframe)+'.jpg')
    for i in range(72):
        for j in range(220):
            if(img[i*5][j*2][1]>100):
                display += '#'
            else:
                display += ' '
        display += '\n'
    
    print(display)
    display = ''
    time.sleep(.05)
    #os.system('cls')
    curframe+=1

