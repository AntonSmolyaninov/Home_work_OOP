from src.product import Product

class Smartphone(Product):
    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 efficiency: float,
                 model: str,
                 memory: int,
                 color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency   # производительность
        self.model = model  # модель
        self.memory = memory  # объем встроенной памяти
        self.color = color  # цвет

    def __add__(self, other: "Smartphone"):
        if type(other) is Smartphone:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError
