import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
                ret, frame = cap.read()
                cv2.imshow("imshow",frame)
                key = cv2.waitKey(20)
                if key==ord('q'):
                       break
                if key==ord('c'):
                       #i+=1
                       cv2.imshow('imshow',frame)
                       cv2.imwrite('C:\\Users\\user7\\Pictures\\cv1.png',frame)
                       print('Wrote')
cap.release()
cv2.destroyAllWindows()
