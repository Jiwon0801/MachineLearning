import cv2
import numpy as np

img = cv2.imread("./image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




cv2.imwrite("./gray_image.jpg", gray)


cv2.imshow("image", gray)
cv2.imshow("color_image", img)



cv2.waitKey()
cv2.destroyAllWindows()