import cv2
# �er�eve boyutlar�n� tan�mla
frameWidth = 640
frameHeight = 360

video = cv2.VideoCapture(r"C:\Users\Furkan\Downloads\video.mp4")

while True:
    success, img = video.read()
    cv2.imshow("video",img)
    
    # 'q' tu�una bas�ld���nda d�ng�den ��k
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# VideoCapture ve pencereleri kapat
video.release()
cv2.destroyAllWindows()