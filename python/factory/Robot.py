from abc import ABC, abstractmethod

class Robot(ABC):

    @abstractmethod
    def orderParts(self):
        pass

    @abstractmethod
    def putTogether(self):
        pass

    @abstractmethod
    def Program(self):
        pass