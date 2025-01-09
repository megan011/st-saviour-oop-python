from cake import Cake 

class StrawberryShortcake(Cake):
    def __init__(self, frosting: bool, size: str):
        super().__init__("Strawberry", frosting, size)