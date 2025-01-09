class BakedGoods: 
    def __init__ (self, flavor: str, frosting: bool):
        self.flavor = flavor
        self.frosting = frosting

    def bake(self, temperature: int):
        print('The ' + self.flavor + ' baked good is in the oven at ' + str(temperature) + ' degrees!')

        