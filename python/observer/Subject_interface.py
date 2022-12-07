from abc import ABC, abstractmethod

class SubjectInterface(ABC):

    @abstractmethod
    def addObserver(self, ob):
        pass
    
    @abstractmethod
    def removeObserver(self, id):
        pass

    @abstractmethod
    def notify(self, news):
        pass

    