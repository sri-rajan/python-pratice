import cv2
import time

img=cv2.VideoCapture(0)

while True:
    check,frame=img.read()
    cv2.imshow("sri",frame)
    Key=cv2.waitKey(1)
    if Key==ord('a'):
        break

    
cv2.destroyAllWindows()
img.release()

