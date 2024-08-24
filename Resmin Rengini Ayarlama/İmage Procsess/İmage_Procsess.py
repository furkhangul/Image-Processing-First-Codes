import cv2
#Ýþin ekstralarýna girecek olursak girdiðimiz resim komutunun yanýna getirdiðimiz farklý sayý veya kombinasyonlar ile resimi deðiþtirebiliyoru. Örnðin
#0 koyduðumuz zaman bu resim renklerinden soyutlanarak gri halini alýyor.
resimUzanti = r"C:\Users\Furkan\source\repos\Resim Okuma\photo.jpg"
#Burada imread komutu resimi oku anlamýna geliyor. Ayrýca bu komut çaðýrýlýrken kendi kütüphanesini yani cv2 kütüphanesini de baþýna alýyor.
resim = cv2.imread(resimUzanti,0)
#Þimdi de okuma iþlemi gerçekleþen resimi görmemiz saðlanýyor. Bunun içinde imshow anahatarýný kullanýyoruz.
cv2.imshow("Resim", resim)
#Bu kod ile ise resimin kapatmadýðýmýz sürece kapanmamasýný saðlýyorum.
cv2.waitKey(0);
#Bu komut bütün pencerelerin kapatýlmasýný saðlýyor.
cv2.destroyAllWindows();

