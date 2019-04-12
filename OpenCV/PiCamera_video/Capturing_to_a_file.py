import time
import picamera

my_file = open('../image_file/image.jpg','wb')

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    #camera.start_preview()
    time.sleep(2)
    camera.capture(my_file)

my_file.close()