from Part_interface import PartInterface

class LaserEyePart(PartInterface):

    def __init__(self) -> None:
        super().__init__()
        self.part_description = "Laser eye"

    def attach(self):
        print(self.part_description, "was attached.")