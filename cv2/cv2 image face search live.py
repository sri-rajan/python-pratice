import cv2
import numpy as np
import time

#create a cascadeclassifier object
face_cascade= cv2.CascadeClassifier(r"C:\Users\SRI RAJAN\Documents\cv2face.xml")

#reading a image as it is
video=cv2.VideoCapture(0)
check,im=video.read()   #check is a inbuilt value to find true or false u can also use anyother name
print(check)
print(im)
time.sleep(3)
video.release()

img=cv2.resize(im,(int(im.shape[1]/2),int(im.shape[0]/2)))

#reading a image as gray scale img
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#search the co-ordinates of the image
faces=face_cascade.detectMultiScale(img,1.3,5,0)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

resized=cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))
cv2.imshow("Gray",resized)
cv2.waitKey(0)

cv2.destroyAllWindows()  
