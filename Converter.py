from abc import ABCMeta, abstractmethod

class Converter(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def convert(self):
        pass