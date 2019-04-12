from vfcamera import VideoFileCamera
from imageviewer import ImageViewer
from imagesender import ImageSender
from queue import Queue

url = 'http://localhost:8080/monitor/camera/1'

queue = Queue(10)

viewer = ImageViewer('image', queue)
sender = ImageSender(url)

camera = VideoFileCamera('../video1.avi', queue)
camera.addObserver(viewer)
camera.addObserver(sender)

camera.start()
viewer.start()
sender.start()