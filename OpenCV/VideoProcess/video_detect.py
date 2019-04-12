import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

while(cap.isOpened()):
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    cascade_file = "haarcascade_upperbody.xml"
    cascade = cv2.CascadeClassifier(cascade_file)

    body_list = cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=1, minSize=(50,50))

    if len(body_list) > 0: # 인식된 영역이 있는가?
        print(body_list)
        # 영역에 사각형 그리기
        color = (0, 0, 255) # 빨간색
        for body in body_list:
            x,y,w,h = body
            cv2.rectangle(frame, (x,y), (x+w, y+h), color, thickness=2)
        #cv2.imwrite("carsdetect-output.avi", frame)
    
    else: # 인식된 영역이 없는 경우
        print("no body")

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()