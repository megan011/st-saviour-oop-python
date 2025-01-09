from baked_goods import BakedGoods

class Cake(BakedGoods):
    def __init__(self, flavor: str, frosting: bool, size: str):
        super().__init__(flavor, frosting)
        self.size = size 