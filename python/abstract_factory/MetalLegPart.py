from Part_interface import PartInterface

class MetalLegPart(PartInterface):

    def __init__(self) -> None:
        super().__init__()
        self.part_description = "Metal Leg"

    def attach(self):
        print(self.part_description, "was attached.")