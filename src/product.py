from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str  # название продукта
    description: str  # описание продукта
    __price: float  # цена продукта
    quantity: int  # колличество в наличии

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if type(other) is Product:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError

    @classmethod
    def new_product(cls, product_info: dict, products: list["Product"]) -> "Product":
        """
        Создаёт новый продукт, если такого ещё нет среди products.
        Если товар с таким же именем уже есть — обновляет количество и (если нужно) цену.
        """
        for existing_product in products:
            if existing_product.name == product_info["name"]:
                # Обновить количество
                existing_product.quantity += product_info.get("quantity", 0)
                # В случае конфликта цен выбираем более высокую цену
                if product_info["price"] > existing_product.price:
                    existing_product.price = product_info["price"]
                return existing_product  # Вернуть обновлённый

        # Если не найден — создать новый объект
        return cls(
            name=product_info["name"],
            description=product_info["description"],
            price=product_info["price"],
            quantity=product_info.get("quantity", 0),
        )

    @property
    def price(self) -> float:
        """Геттер для атрибута цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для атрибута цены с проверкой."""
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная.")
        self.__price = value
