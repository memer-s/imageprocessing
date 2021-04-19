import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(sys.argv[1])
arg2 = int(sys.argv[2])

num = 0
nam = 0

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    num += 1
    
    if(arg2>1):
        if(num%arg2==0):
            nam+=1
            cv2.imwrite('frame'+str(nam)+'.jpg', frame)
    else:
        nam+=1
        cv2.imwrite('frame'+str(nam)+'.jpg', frame)
    

cap.release()
cv2.destroyAllWindows()