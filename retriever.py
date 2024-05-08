from abc import ABCMeta, abstractmethod

class VideoRetriever(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def search(self):
        pass