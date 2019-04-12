import cv2

img = cv2.imread("image.jpg")

img_crop= img[0:200, 150:350] #(0,150) (200,350)
cv2.imshow("resize", img_crop)

cv2.waitKey()
cv2.destroyAllWindows()