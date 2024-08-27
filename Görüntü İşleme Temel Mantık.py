#Görüntü işleme üzerine birden fazla örnek yaptım fakat bu görüntü işlemenin temel mantığını oturtmamda yardımcı olmayacak bunun için bilgisayarın hangi işlemlerden geçerek bu işlemenin yapıldığını anlamam lazım.
#Görüntü işleme denilen olay aslında çekirdeğe okutmak için gönderdiğimiz resmin pixel pixel şekilde bellekte tutulması anlamına geliyor.
#Bütün renklerin mavi, kırmızı ve yeşil renklerinden türediğini biliyoruz bunun için makine kendine 3 renk tonlamasının 225'e kadar alabileceği değerlerde karışımını bellekte tutuyor.
#Örneğin hafızada bir pixeli = [115 0 75 ] şeklinde tutuyor. 115 blue yani mavi değeri, 0 green yani yeşil değeri, 75 red yani kırmızı değeri ifade ediyor.
#Burada binlerce pixelli bir resimi bu şekilde kodlayarak istediği rengi istediğimiz şekilde kodlayabiliyor.

import cv2

path=r"C\User\Furkan\Download\img.jpg"
img = cv2.imread(path)
#Bu ifade gönderdiğimiz resmin bize işlenmiş kodlarını çıktı olarak vermesini sağlıyor.
print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
