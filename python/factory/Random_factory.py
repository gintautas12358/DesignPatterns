from Simple_robot_factory import SimpleRobotFactory
from ToyRobot import ToyRobot
from TerminatorRobot import TerminatorRobot
 
class RandomFactory(SimpleRobotFactory):

    def __init__(self) -> None:
        super().__init__()

    def createRobot(self, type):
        if type == "ToyRobot":
            r = ToyRobot()
        elif type == "TerminatorRobot":
            r = TerminatorRobot()  
        else:
            print("no such type")
        return r