import cv2

img = cv2.imread("./image.jpg")
print(img.shape)
cv2.imshow("image",img)

cv2.waitKey()
cv2.destroyAllWindows()