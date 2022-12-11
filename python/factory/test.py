from Agency import Agency
from Random_factory import RandomFactory

f = RandomFactory()
a = Agency(f)
a.createRobot("ToyRobot")
a.createRobot("TerminatorRobot")