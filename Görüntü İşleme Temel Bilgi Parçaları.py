import cv2

path=r"C\User\Furkan\Download\img.png"
img = cv2.imread(path)


#Bu komut bize resmin pixel pixel kodlarını verir.
print(img)

#Bu komut bize resmin hangi şekilde basıldığını gösterir. Örneğin <class = 'numby.ndarray'> şeklinde numpy şeklinde sıralandığını gösteriyor.
#Numpy ndarray: bilimsel hesaplamaların hızlı bir şekilde yapıldığı matematik kütüphanesidir.  Numpy'ın temelini numpy dizileri oluşturur. Python dizilerinden farklı olarakta dizler homojen şekildedir.
#yani dizideki elemanlar aynı veri tipinde yazılır.
print(type(img))

#Bu komut yazıldığı zaman bize (640 , 360, 3) şeklinde bir kod geliyor 640 yüksekliği ifade ediyor, 360 genişliği ifade ediyor, 3 ise kullanılan renk sayısını ifade ediyor. shape = şekil 
print(img.shape)

#Resmin yüksekliği ile resmin genişlik ve renk kanalı sayısnı çarptığımız zaman bize bir değer verir. Bu değer resmin boyutunu verir.
print(img.size)

#Bu kod bize resim hakkında bilgi verir. Örnek olarak çıkacak kod : uint8 şeklinde bir kod olacaktır. Buradaki int değeri intager, u unside, 8 ise 8 bit anlamına geliyor. renk aralığımızın 255 olmasının sebebi 2^8 değerinin 256 dğerine denk gelmesidir.
#Örnek olarak ele alırsak: [ 0 0 0 0 0 0 0 0 ]şeklinde bütün bitler 0 olursa siyah renk ortaya çıkmaktadır. [ 1 1 1 1 1 1 1 1 ] şeklinde bütün bitler 1 olursa beyaz rengi elde etmiş oluruz.
print(img.dtype)
