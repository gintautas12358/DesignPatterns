from Product_ingredient_interface import ProductIngredientInterface

class HenzKetchup(ProductIngredientInterface):

    def __init__(self, product) -> None:
        super().__init__()
        self.product = product

    def price(self):
        return self.product.price() + 4.00

    def get_ingredient(self):
        return self.product.get_ingredient() + ", with Henz ketchup"
