from Part_interface import PartInterface

class LEDPart(PartInterface):

    def __init__(self) -> None:
        super().__init__()
        self.part_description = "LED"

    def attach(self):
        print(self.part_description, "was attached.")