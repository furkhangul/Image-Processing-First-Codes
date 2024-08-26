import cv2
# Çerçeve boyutlarýný tanýmla
frameWidth = 640
frameHeight = 100

video = cv2.VideoCapture(r"C:\Users\Furkan\Downloads\video.mp4")

while True:
    success, img = video.read()
    img = cv2.resize(img,(frameHeight,frameWidth))
    cv2.imshow("video",img)
    # 'q' tuþuna basýldýðýnda döngüden çýk
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# VideoCapture ve pencereleri kapat
video.release()
cv2.destroyAllWindows()