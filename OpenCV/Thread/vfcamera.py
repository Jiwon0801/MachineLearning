import cv2 
from threading import Thread
from observer import Observerable

class VideoFileCamera(Observerable, Thread):
    def __init__(self, video_file, queue):
        Thread.__init__(self)
        Observerable.__init__(self)

        self.video_file = video_file

    def run(self):
        cap = cv2.VideoCapture(self.video_file)
        fps = cap.get(cv2.CAP_PROP_FPS)
        delay = int(1000/fps)
        while(cap.isOpened()):
            ret, frame = cap.read()
            self.notifyAll(frame)
            cv2.waitKey(delay)

        cap.release()