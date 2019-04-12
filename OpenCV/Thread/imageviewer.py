from threading import Thread
from queue import Queue
import requests 
import cv2 
from observer import Observer


class ImageViewer(Thread, Observer) :
    def __init__(self, name, queue):
        Thread.__init__(self)
        self.name = name
        self.queue = Queue(10)
       
    def update(self, data):
        self.queue.put(data, timeout=2)

    def run(self):
        while(True) :
            image = self.queue.get(timeout=2)
            cv2.imshow(self.name,image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()