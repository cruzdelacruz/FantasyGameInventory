class game_item():
    def __init__(self, name: str, quantity: int, weight: float):
        self.name = name
        self.quantity = quantity
        self.weight = weight
        
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name},quantity={sel.quantity},weight={self.weight}kg)"
      