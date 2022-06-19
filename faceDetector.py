import cv2
face_casecade = cv2.CasecadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("photo.jpg")
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

