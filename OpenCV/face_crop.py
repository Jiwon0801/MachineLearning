import numpy as np
import cv2

def get_face_crop(face, area):
    x, y, w, h = area
    ex, ey = x+w, y+h
    
    gap = int(abs((w-h)/2))

    # 크기 조정
    if w > h : # y 좌표 조정
        y = y- gap
        ey = ey + gap
    else : # x 좌표 조정
        x = x - gaps
        ex = ex + gap

    print(x, y, ex, ey, (ex-x), (ey-y))

    # crop
    face= face[y: ey, x: ex]

    return face

def get_face(img, area):
    face = get_face_crop(img, area)
    # 크기 변환
    face = cv2.resize(face, (28, 28), interpolation = cv2.INTER_AREA)
    # 회색 변환
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    return face


if __name__ == "__main__":
    img= cv2.imread('face1.jpg')
    face_area = [430, 450, 250, 400]

    face = get_face(img, face_area)
    cv2.imshow("face", face)

    cv2.waitKey()
    cv2.destroyAllWindows()
