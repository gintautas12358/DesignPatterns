from abc import ABC, abstractmethod

class TargetInterface(ABC):

    @abstractmethod
    def is_alive(self) -> bool:
        pass

    abstractmethod
    def modify_survivability(self, modifier):
        pass

    @abstractmethod
    def got_shoted(self):
        pass