from Robot import Robot
from PlasticLegPart import PlasticLegPart
from LEDPart import LEDPart

class ToyRobot(Robot):

    def __init__(self, part_factory) -> None:
        super().__init__()
        self.parts = []
        self.part_factory = part_factory

    def orderParts(self):
        print("Simple flushy parts")
        for p in self.part_factory.parts:
            self.parts.append(p)
        # self.parts.append(LEDPart())
        # self.parts.append(PlasticLegPart())
        return self.parts

    def putTogether(self, parts):
        print("Sew it together")
        for p in parts:
            p.attach()

    def Program(self):
        print("Programmed to love")