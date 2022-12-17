from Joe import Joe
from JoeAlien import JoeAlien
from Human_adapter import HumanAdapter

def humans_interacting(h1, h2):
    h1.talk()
    h2.gesture()
    print()
    h2.talk()
    h1.gesture()
    h1.talk()
    print("== end of interaction ==")
    print()

joe1 = Joe()
joe2 = Joe()
ajoe = JoeAlien()

humans_interacting(joe1, joe2)
humans_interacting(joe1, HumanAdapter(ajoe))
