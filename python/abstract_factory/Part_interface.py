from abc import ABC, abstractmethod

class PartInterface(ABC):

    @abstractmethod
    def attach(self):
        pass
