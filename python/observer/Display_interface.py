from abc import ABC, abstractmethod

class DisplayInterface(ABC):

    @abstractmethod
    def display(self):
        pass