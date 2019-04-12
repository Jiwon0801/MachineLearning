import cv2
import sys

image_file = "face1.jpg"
image = cv2.imread(image_file)
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 인식 특징 파일 읽어 들이기
cascade_file = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

# 얼굴 인식 실행하기
face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(150,150))

if len(face_list) > 0: # 인식된 영역이 있는가?
    print(face_list)
    # 얼굴 영역에 사각형 그리기
    color = (0, 0, 255) # 빨간색
    for face in face_list:
        x,y,w,h = face
        cv2.rectangle(image, (x,y), (x+w, y+h), color, thickness=8)
    cv2.imwrite("facedetect-output.PNG", image)
    
else: # 인식된 영역이 없는 경우
    print("no face")
