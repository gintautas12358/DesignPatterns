from abc import ABC, abstractmethod

class ToolInterface(ABC):

    @abstractmethod
    def use(self):
        pass

