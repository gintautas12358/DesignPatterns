from abc import ABC, abstractmethod

class SimpleRobotFactory(ABC):

    @abstractmethod
    def createRobot(self, type):
        pass