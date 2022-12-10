from Havana_pizza import HavanaPizza
from Mozzerela import Mozzerela
from Henz_ketchup import HenzKetchup

p = HavanaPizza()
p = Mozzerela(p)
p = HenzKetchup(p)

print("Total price: ", p.price())
print("Ingredients: ", p.get_ingredient())