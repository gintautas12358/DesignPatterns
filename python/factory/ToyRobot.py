from Robot import Robot

class ToyRobot(Robot):

    def __init__(self) -> None:
        super().__init__()

    def orderParts(self):
        print("Simple flushy parts")

    def putTogether(self):
        print("Sew it together")

    def Program(self):
        print("Programmed to love")