import io
import time
import picamera
import cv2
import numpy as np
import requests

url = 'http://localhost:8080/monitor/camera/1'

with picamera.PiCamera() as camera:
    time.sleep(2)
    camera.resolution = (320, 240)
    with io.BytesIO() as stream:
        while(True):
            camera.capture(stream, format='jpeg', use_video_port=True)
            stream.seek(0)
            res = requests.post(url,files={'image':stream})
            stream.seek(0)
            stream.truncate()