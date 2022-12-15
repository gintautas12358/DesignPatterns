from Simple_robot_factory import SimpleRobotFactory
from ToyRobot import ToyRobot
from TerminatorRobot import TerminatorRobot
from KukaPartFactory import KukaPartFactory
 
class RandomFactory(SimpleRobotFactory):

    def __init__(self, part_factory) -> None:
        super().__init__()
        self.part_factory = part_factory

    def createRobot(self, type):
        if type == "toy":
            r = ToyRobot(self.part_factory)
            print()
        elif type == "future":
            r = TerminatorRobot(self.part_factory)  
            print()
        else:
            print("no such type")
        return r