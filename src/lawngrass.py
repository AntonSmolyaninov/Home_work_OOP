from src.product import Product

class LawnGrass(Product):

    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 country: str,
                 germination_period: str,
                 color: str,) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country  # страна - производитель
        self.germination_period = germination_period  # срок проростания
        self.color = color  # цвет

    def __add__(self, other) -> float:
        if type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError









