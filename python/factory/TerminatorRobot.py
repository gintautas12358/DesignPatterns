from Robot import Robot

class TerminatorRobot(Robot):

    def __init__(self) -> None:
        super().__init__()

    def orderParts(self):
        print("Order heavy cutting edge parts")

    def putTogether(self):
        print("Big team of engineers to to put it together")

    def Program(self):
        print("Years of programming")