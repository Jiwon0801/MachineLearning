import cv2

img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th_value, new_img = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
cv2.imshow("image", new_img)


cv2.waitKey()
cv2.destroyAllWindows()

