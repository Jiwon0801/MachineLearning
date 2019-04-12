import cv2
import numpy as np
img = cv2.imread("image.jpg")
ker = np.array([
[1, 1, 1],
[1, 1, 1],
[1, 1, 1]
])
# ker = np.ones((3, 3))
# ker = np.random.rand(3, 3)
new_img = cv2.filter2D(img, -1, ker)
cv2.imshow("image", new_img)
cv2.waitKey()
cv2.destroyAllWindows()