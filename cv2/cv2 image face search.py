import cv2
import numpy as np

#create a cascadeclassifier object
face_cascade= cv2.CascadeClassifier(r"C:\Users\SRI RAJAN\Documents\cv2face.xml")

#reading a image as it is
im=cv2.imread(r"D:\whatsapp pic\IMG-20191202-WA0004.jpg")
img=cv2.resize(im,(int(im.shape[1]/2),int(im.shape[0]/2)))

#reading a image as gray scale img
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#search the co-ordinates of the image
faces=face_cascade.detectMultiScale(gray,1.1,5,0)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)

resized=cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))
cv2.imshow("Gray",resized)
cv2.waitKey(0)

cv2.destroyAllWindows()                   


