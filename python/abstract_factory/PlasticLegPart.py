from Part_interface import PartInterface

class PlasticLegPart(PartInterface):

    def __init__(self) -> None:
        super().__init__()
        self.part_description = "Plastic Leg"

    def attach(self):
        print(self.part_description, "was attached.")