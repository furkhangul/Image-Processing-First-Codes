import cv2

resimUzanti = r"C:\Users\Furkan\source\repos\Resim Okuma\photo.jpg"
#Burada imread komutu resimi oku anlam�na geliyor. Ayr�ca bu komut �a��r�l�rken kendi k�t�phanesini yani cv2 k�t�phanesini de ba��na al�yor.
resim = cv2.imread(resimUzanti)
#�imdi de okuma i�lemi ger�ekle�en resimi g�rmemiz sa�lan�yor. Bunun i�inde imshow anahatar�n� kullan�yoruz.
cv2.imshow("Resim", resim)
#Bu kod ile ise resimin kapatmad���m�z s�rece kapanmamas�n� sa�l�yorum.
cv2.waitKey(0);
