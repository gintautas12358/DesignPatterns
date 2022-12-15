from PlasticLegPart import PlasticLegPart
from LEDPart import LEDPart
from PartFactory_interface import PartFactoryInterface

class KukaPartFactory(PartFactoryInterface):

    def __init__(self) -> None:
        self.parts = [PlasticLegPart(), LEDPart()]
        for p in self.parts:
            p.part_description = "Kuka " + p.part_description