import cv2
#İşin ekstralarına girecek olursak girdiğimiz resim komutunun yanına getirdiğimiz farklı sayı veya kombinasyonlar ile resimi değiştirebiliyoru. Örnğin
#0 koyduğumuz zaman bu resim renklerinden soyutlanarak gri halini alıyor.
resimUzanti = r"C:\Users\Furkan\source\repos\Resim Okuma\photo.jpg"
#Burada imread komutu resimi oku anlamına geliyor. Ayrıca bu komut çağırılırken kendi kütüphanesini yani cv2 kütüphanesini de başına alıyor.
resim = cv2.imread(resimUzanti,0)
#Şimdi de okuma işlemi gerçekleşen resimi görmemiz sağlanıyor. Bunun içinde imshow anahatarını kullanıyoruz.
cv2.imshow("Resim", resim)
#Bu kod ile ise resimin kapatmadığımız sürece kapanmamasını sağlıyorum.
cv2.waitKey(0);
#Bu komut bütün pencerelerin kapatılmasını sağlıyor.
cv2.destroyAllWindows();

#Bu komut ile yenilediğimiz resmi kayıdedebiliyoruz. Renk ayarları birden fazla da olaiblir.
cv2.imwrite("yenigorsel.jpg0",resim)
