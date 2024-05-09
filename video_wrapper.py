from abc import ABCMeta, abstractmethod

class VideoWrapper(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def download(self):
        pass