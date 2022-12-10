from abc import ABC, abstractmethod

class ProductIngredientInterface(ABC):

    @abstractmethod
    def price(self) -> bool:
        pass

    abstractmethod
    def get_ingredient(self):
        pass
