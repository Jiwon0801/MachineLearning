import io 
import time
import picamera
import picamera.array
import cv2

# Create an in-memory stream
my_stream = io.BytesIO()

with picamera.PiCamera() as camera:
    #camera.start_preview()
    camera.resolution = (640, 480)
    with picamera.array.PiRGBArray(camera) as stream:
        # fps 처리
        time.sleep(2)
        start = time.time()
        count = 0

        while(time.time()-start < 1):
            camera.capture(my_stream, format='bgr', use_video_port=True)
            image = stream.array
            count += 1
            stream.seek(0)
            stream.truncate()

        print('fps: ', count)
        