from Target_interface import TargetInterface
import random

class Elk(TargetInterface):

    def __init__(self) -> None:
        super().__init__()
        

    def is_alive(self):
        return random.random() < 0.7