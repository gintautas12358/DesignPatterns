from Tool_interface import ToolInterface

class HuntingOdour(ToolInterface):

    def __init__(self) -> None:
        super().__init__()
        self.uses = 2
        self.target_modifier = 0.9

    def use(self, target):
        if self.uses:
            self.uses = self.uses - 1
            target.modify_survivability(self.target_modifier)
        else:
            print("Bottle is empty.")