from abc import ABCMeta, abstractmethod

class Video(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def download(self):
        pass