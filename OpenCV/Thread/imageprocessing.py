from threading import Thread
import cv2
from queue import Queue
from observer import Observer

class ImageProcessing(Thread, Observer) :
    def __init__(self):
        Thread.__init__(self)
        self.queue = Queue(10)
        
    def update(self, data):
        self.queue.put(data, timeout=2)
        
    def run(self):
        while(True) :
            image = self.queue.get(timeout=2)
            # 이미지 처리