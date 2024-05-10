from abc import ABCMeta, abstractmethod

class MetricAnalyzer(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def analyse(self):
        pass