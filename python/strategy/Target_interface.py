from abc import ABC, abstractmethod

class TargetInterface(ABC):

    @abstractmethod
    def is_alive(self) -> bool:
        pass

    