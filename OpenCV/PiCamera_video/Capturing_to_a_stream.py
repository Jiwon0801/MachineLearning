import io 
import time
import picamera

# Create an in-memory stream
my_stream = io.BytesIO()

with picamera.PiCamera() as camera:
    #camera.start_preview()
    time.sleep(2)
    start = time.time()
    count = 0

    while(time.time()-start  1):
        camera.capture(my_stream, 'jpeg')
        count += 1

    print('fps: ', count)

    # Camera warm-up time
    #time.sleep(2)
    #camera.capture(my_stream, 'jpeg')