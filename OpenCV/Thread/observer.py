from abc import *
class Observerable :
    def __init__(self):
        self.observers = []

    def addObserver(self, observer):
        self.observers.append(observer)

    def deleteObserver(self, observer):
        self.observers.remove(observer)
        
    def notifyAll(self, data) :
        for observer in self.observers:
            observer.update(data)
    
# Observer 추상 클래스
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, data):
        pass