from Agency import Agency
from Random_factory import RandomFactory
from KukaPartFactory import KukaPartFactory
from ABBPartFactory import ABBPartFactory

pf = KukaPartFactory()
f = RandomFactory(pf)
a = Agency(f)
a.createRobot("toy")
a.createRobot("future")

pf2 = ABBPartFactory()
f2 = RandomFactory(pf2)
a2 = Agency(f2)
a2.createRobot("toy")
a2.createRobot("future")