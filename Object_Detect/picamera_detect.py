import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
from detecter import Detecter

THRESHOLD = 0.3
detecter = Detecter()
detecter.setup('./frozen_inference_graph.pb', './mscoco_label_map.pbtxt')

# 파이카메라 준비
# 카메라 해상도
IM_WIDTH = 640
IM_HEIGHT = 480

# PiCamera 설정
camera = PiCamera()
camera.resolution = (IM_WIDTH,IM_HEIGHT)
camera.framerate = 10

rawCapture = PiRGBArray(camera, size=(IM_WIDTH,IM_HEIGHT))
rawCapture.truncate(0)

for frame1 in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
    image = np.copy(frame1.array)
    image.setflags(write=1)
    image_ex = np.expand_dims(image, axis=0)
    # detection
    (boxes, scores, classes, num) = detecter.detect(image_ex)
    # 시각화
    (boxes, scores, classes) = (np.squeeze(boxes), np.squeeze(scores), np.squeeze(classes).astype(np.uint8))
    detecter.visualize(image, boxes, classes, scores, THRESHOLD)
    
    # 이미지 출력
    cv2.imshow('Object detector', image)
    if cv2.waitKey(1) == ord('q'): break
    rawCapture.truncate(0)

camera.close()
cv2.destroyAllWindows()