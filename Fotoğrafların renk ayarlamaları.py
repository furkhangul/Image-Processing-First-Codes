import cv2 
import numpy as np

path = r"C\User\Furkan\Downloads\img.jpg"

img = cv2.imread(path)

#Bu kod fotoğradın gri şeklinde yapılandırılmasını sağlar
GrayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Bu kod fotoğrafın buğulu bir şekilde oluşmasını sağlar
BuguImage = cv2.GaussianBlur(img,(5,5),5)

#Bu kod fotoğrafın siyah arka planda çizgilerin ana hatlarını ortaya koyar.
CannyImage = cv2.Canny(img,100,100)

#Bu kod hatları çıkan fotoğrafın hatlarını kalınlaştırmaya yarar.
GenerateImage = cv2.dilate(CannyImage,kernel)

cv2.imshow(img)
cv2.imshow(GrayImage)
cv2.imshow(BuguImage)
cv2.imshow(CannyImage)
cv2.imshow(GenerateImage)


cv2.waitKey(0)
cv2.destroyAllWindows()


