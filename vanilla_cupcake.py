from cupcake import Cupcake 

class VanillaCupcake(Cupcake):
    def __init__(self, frosting: str, liner: str):
        super().__init__("Vanilla", liner, frosting)
