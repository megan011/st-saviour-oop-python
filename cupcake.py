from baked_goods import BakedGoods

class Cupcake(BakedGoods):  
    def __init__(self, flavor: str, liner: str, frosting: str):
        super().__init__(flavor, True)    
        self.flavor = flavor
        self.frosting = frosting
        self.liner = liner 

    def decorate(self):
        print(f"The cupcake is decorated with {self.frosting} frosting!")

    def __str__(self):
        return f'flavor: {self.flavor}, frosting: {self.frosting}, liner: {self.liner}'