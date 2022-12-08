from abc import ABC, abstractmethod

class GunInterface(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def shoot(self, target):
        pass


    