import cv2
im=cv2.imread(r"C:\Users\SRI RAJAN\Downloads\1217655.jpg")
img=cv2.resize(im,(int(im.shape[1]/2),int(im.shape[0]/2)))
cv2.imshow("sri",img)
cv2.waitKey(2000)
cv2.destroyAllWindows()
