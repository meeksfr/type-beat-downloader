from abc import ABCMeta, abstractmethod

class UserTaste(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def getSearchTerms(self):
        pass