import numpy as np
import cv2
from detecter_image import get_detect_image
from detecter import Detecter

cap = cv2.VideoCapture('video2.avi')
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

THRESHOLD = 0.25

detecter = Detecter()
detecter.setup('./frozen_inference_graph.pb', './mscoco_label_map.pbtxt')

while(cap.isOpened()):
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_ex = np.expand_dims(frame, axis=0)
    (boxes, scores, classes, num) = detecter.detect(frame_ex)
    detecter.visualize(frame, boxes, classes, scores, THRESHOLD)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()