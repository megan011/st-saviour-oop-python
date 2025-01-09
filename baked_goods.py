class BakedGoods: 
    def __init__(self, flavor: str, frosting: bool):
        self.flavor = flavor
        self.frosting = frosting
        self.toppings = []

    def bake(self, temperature: int):
        print('The ' + self.flavor + ' baked good is in the oven at ' + str(temperature) + ' degrees!')

    def add_toppings(self, *args):
        for arg in args:
            self.toppings.append(arg)

        