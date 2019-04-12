import numpy as np
import cv2

cap = cv2.VideoCapture('video2.avi')
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

while(cap.isOpened()):
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    body_cascade_file = "haarcascade_upperbody.xml"
    car_cascade_file = "cars.xml"
    body_cascade = cv2.CascadeClassifier(body_cascade_file)
    car_cascade = cv2.CascadeClassifier(car_cascade_file)

    body_list = body_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=1, minSize=(5,5))
    car_list = car_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=1, minSize=(50,50))


    ### body
    if len(body_list) > 0: # 인식된 영역이 있는가?
        print(body_list)

        # 영역에 사각형 그리기
        body_color = (0, 0, 255) # 빨간색
      
        for body in body_list:
            x,y,w,h = body
            cv2.rectangle(frame, (x,y), (x+w, y+h), body_color, thickness=2)
        
        #cv2.imwrite("carsdetect-output.avi", frame)
    
    else: # 인식된 영역이 없는 경우
        print("no body")
    
    ### car
    if len(car_list) > 0: # 인식된 영역이 있는가?
       
        print(car_list)
        # 영역에 사각형 그리기
        
        car_color = (255, 0, 0 ) #파란색
       
        for car in car_list:
            x,y,w,h = car
            cv2.rectangle(frame, (x,y), (x+w, y+h), car_color, thickness=2)
        #cv2.imwrite("carsdetect-output.avi", frame)
    
    else: # 인식된 영역이 없는 경우
        print("no car")

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()