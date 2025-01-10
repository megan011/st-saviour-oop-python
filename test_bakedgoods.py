from baked_goods import BakedGoods
from cupcake import Cupcake
from vanilla_cupcake import VanillaCupcake
from strawberry_shortcake import StrawberryShortcake
from cake import Cake

def test_cake():
    my_cake = Cake('vanilla', True)
    my_cake.bake(350)
    my_cake.add_toppings('gummy bears', 'sprinkles')
    assert len(my_cake.toppings) == 2 

    my_cupcake = Cupcake('vanilla', 'wax', 'vanilla')
    assert isinstance(my_cupcake, Cupcake)
    assert isinstance(my_cupcake, BakedGoods)