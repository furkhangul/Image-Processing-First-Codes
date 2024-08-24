import cv2
#��in ekstralar�na girecek olursak girdi�imiz resim komutunun yan�na getirdi�imiz farkl� say� veya kombinasyonlar ile resimi de�i�tirebiliyoru. �rn�in
#0 koydu�umuz zaman bu resim renklerinden soyutlanarak gri halini al�yor.
resimUzanti = r"C:\Users\Furkan\source\repos\Resim Okuma\photo.jpg"
#Burada imread komutu resimi oku anlam�na geliyor. Ayr�ca bu komut �a��r�l�rken kendi k�t�phanesini yani cv2 k�t�phanesini de ba��na al�yor.
resim = cv2.imread(resimUzanti,0)
#�imdi de okuma i�lemi ger�ekle�en resimi g�rmemiz sa�lan�yor. Bunun i�inde imshow anahatar�n� kullan�yoruz.
cv2.imshow("Resim", resim)
#Bu kod ile ise resimin kapatmad���m�z s�rece kapanmamas�n� sa�l�yorum.
cv2.waitKey(0);
#Bu komut b�t�n pencerelerin kapat�lmas�n� sa�l�yor.
cv2.destroyAllWindows();

