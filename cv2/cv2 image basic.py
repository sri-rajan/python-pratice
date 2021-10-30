import cv2

img=cv2.imread("C:\\Users\\SRI RAJAN\\Downloads\\1217655.jpg",1)
resizeimg=cv2.resize(img,(600,600))
resize2=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("sri",resizeimg)
cv2.imshow("sri2",resize2)

cv2.waitKey(0)
# cv2.waitKey(2000)   ... it will close window after 2000milisec

cv2.destroyAllWindows()
