class Product:
    name: str
    description: str
    price: float
    quantity: int
    

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, product_info: dict) -> 'Product':
        """Принимает параметры товара в словаре и возвращает созданный объект класса Product"""
        return cls(
            name=product_info['name'],
            description=product_info['description'],
            price=product_info['price'],
            quantity=product_info.get('quantity', 0)
        )


    @property
    def price(self) -> float:
        """Геттер для атрибута цены."""
        return self.__price  # Возвращаем приватный атрибут цены

    @price.setter
    def price(self, value: float):
        """Сеттер для атрибута цены с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная.")
            return
        self.__price = value
