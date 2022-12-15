from Robot import Robot
from MetalLegPart import MetalLegPart
from LEDPart import LEDPart
from LaserPart import LaserEyePart

class TerminatorRobot(Robot):

    def __init__(self, part_factory) -> None:
        super().__init__()
        self.parts = []
        self.part_factory = part_factory

    def orderParts(self):
        print("Order heavy cutting edge parts")
        for p in self.part_factory.parts:
            self.parts.append(p)
        self.parts.append(LaserEyePart())
        return self.parts

    def putTogether(self, parts):
        print("Big team of engineers to to put it together")
        for p in parts:
            p.attach()

    def Program(self):
        print("Years of programming")