from face_module import get_face
import cv2

img= cv2.imread('./face1.jpg')
face_area = [430, 450, 250, 400]

face = get_face(img, face_area)
cv2.imshow("face", face)

cv2.waitKey()
cv2.destroyAllWindows()