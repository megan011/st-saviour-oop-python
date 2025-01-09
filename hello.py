from cupcake import Cupcake
from baked_goods import BakedGoods
from vanilla_cupcake import VanillaCupcake
from strawberry_shortcake import StrawberryShortcake

if __name__ == '__main__':
    # print('new dawn, new day')
    my_baked_good = BakedGoods('vanilla', True)
    my_baked_good.bake(350)
    my_baked_good.add_toppings('gummy bears', 'sprinkles')
    print('toppings: ' + str(my_baked_good.toppings))

    my_cupcake = Cupcake('chocolate', 'wax', 'vanilla')
    print(str(my_cupcake))
