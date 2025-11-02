class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self._price = self._validate_price(price)  # Приватный атрибут для цены
        self.quantity = self._validate_quantity(quantity)

    @staticmethod
    def _validate_price(price: float) -> float:
        """Проверяет и возвращает цену."""
        if price <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной.")
        return price

    @staticmethod
    def _validate_quantity(quantity: int) -> int:
        """Проверяет и возвращает количество."""
        if quantity < 0:
            raise ValueError("Количество не должно быть отрицательным.")
        return quantity

    @property
    def price(self) -> float:
        """Геттер для атрибута цены."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для атрибута цены с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная.")
        else:
            self._price = value  # Устанавливаем новую цену

    @classmethod
    def new_product(cls, product_info: dict) -> 'Product':
        """Создает новый продукт на основе данных из словаря."""
        return cls(
            name=product_info['name'],
            description=product_info['description'],
            price=product_info['price'],
            quantity=product_info.get('quantity', 0)
        )

    @property
    def products(self) -> str:
        """Геттер для строки с информацией о продукте."""
        return f"{self.name}, {self.price:.2f} руб. Остаток: {self.quantity} шт."