from abc import ABC, abstractmethod

class BakedGoods(ABC): 
    def __init__(self, flavor: str, frosting: bool):
        self.flavor = flavor
        self.frosting = frosting
        self.toppings = []

    @abstractmethod
    def bake(self, temperature: int):
        pass
    
    def add_toppings(self, *args):
        for arg in args:
            self.toppings.append(arg)
