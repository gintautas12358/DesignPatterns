from abc import ABC, abstractmethod

class PartFactoryInterface(ABC):

    def __init__(self) -> None:
        self.parts = []
