from Target_interface import TargetInterface
import random

class Elk(TargetInterface):

    def __init__(self) -> None:
        super().__init__()
        self.survivability = 0.7
        self.is_living = True

    def got_shoted(self):
        self.is_living =  random.random() < self.survivability

    def modify_survivability(self, modifier):
        self.survivability *= modifier

    def is_alive(self) -> bool:
        return self.is_living