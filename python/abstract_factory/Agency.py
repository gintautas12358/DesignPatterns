from Simple_robot_factory import SimpleRobotFactory

class Agency:

    def __init__(self, factory) -> None:
        self.factory = factory

    def createRobot(self, type):
        r = self.factory.createRobot(type)
        parts = r.orderParts()
        r.putTogether(parts)
        r.Program()
        return r
        
    