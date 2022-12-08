from Tool_interface import ToolInterface

class HuntingOdour(ToolInterface):

    def __init__(self) -> None:
        super().__init__()
        self.uses = 2

    def use(self):
        if self.uses:
            self.uses = self.uses - 1
        else:
            print("Bottle is empty.")