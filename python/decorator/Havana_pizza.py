from Product_ingredient_interface import ProductIngredientInterface

class HavanaPizza(ProductIngredientInterface):

    def __init__(self) -> None:
        super().__init__()

    def price(self):
        return 7.80

    def get_ingredient(self):
        return "Havana pizzy"
