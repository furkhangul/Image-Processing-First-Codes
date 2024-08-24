import cv2

resimUzanti = r"C:\Users\Furkan\source\repos\Resim Okuma\photo.jpg"
#Burada imread komutu resimi oku anlamına geliyor. Ayrıca bu komut çağırılırken kendi kütüphanesini yani cv2 kütüphanesini de başına alıyor.
resim = cv2.imread(resimUzanti)
#Şimdi de okuma işlemi gerçekleşen resimi görmemiz sağlanıyor. Bunun içinde imshow anahatarını kullanıyoruz.
cv2.imshow("Çerçeve Adı Ne Olsun", resim)
#Bu kod ile ise resimin kapatmadığımız sürece kapanmamasını sağlıyorum.
cv2.waitKey(0);
