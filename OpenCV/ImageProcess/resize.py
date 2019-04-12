import cv2

img = cv2.imread("image.jpg")
r,c = img.shape[:2]
#new_img = cv2.resize(img, (2*r, 2*c), interpolation = cv2.INTER_CUBIC)
new_img = cv2.resize(img, (32, 32), interpolation = cv2.INTER_AREA)

cv2.imshow("resize",new_img)

cv2.waitKey()
cv2.destroyAllWindows()