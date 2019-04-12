import cv2
import numpy as np

img = cv2.imread("image.jpg")
r,c = img.shape[0:2]
M = cv2.getRotationMatrix2D((c/2, r/2), 90, -1) # 1 : 반시계 방향, -1 : 시계방향
new_img = cv2.warpAffine(img, M, (c, r))
cv2.imshow("image", new_img)
cv2.waitKey()
cv2.destroyAllWindows()