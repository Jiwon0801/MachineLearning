from vfcamera import VideoFileCamera
from imageviewer import ImageViewer
from queue import Queue

queue = Queue(10)

viewer = ImageViewer("image", queue)
viewer.start()

camera = VideoFileCamera('../video1.avi', queue)
camera.start()