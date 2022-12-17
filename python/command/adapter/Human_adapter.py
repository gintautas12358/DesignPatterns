from Human_interface import HumanInterface

class HumanAdapter(HumanInterface):

    def __init__(self, alien) -> None:
        self.alien = alien

    def talk(self):
        self.alien.squick()

    def gesture(self):
        self.alien.transform()