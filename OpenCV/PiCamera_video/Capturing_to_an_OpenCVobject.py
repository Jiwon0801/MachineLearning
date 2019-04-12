import io
import time
import picamera
import cv2
import numpy as np

stream = io.BytesIO()

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format='jpeg')
    
    # 스트림에서 numpy 배열로 변환
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    
    # OpenCV 이미지로 변환, BGR 순서
    image = cv2.imdecode(data, 1)
    cv2.imshow("image",image)

    cv2.waitKey()
    cv2.destroyAllWindows()
    
    # RGB를 원하는 경우
    image = image[:, :, ::-1]