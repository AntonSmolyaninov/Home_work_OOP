from src.Product import Product


class Category:

    name: str  # название
    description: str  # описание
    __products: list[Product]  # приватный атрибут, список товаров
    category_count: int = 0  # количество категорий
    product_count: int = 0  # количество товаров

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {Category.product_count} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в список товаров"""
        self.__products.append(product)
        Category.product_count += 1  # Увеличиваем счетчик

    @property
    def products(self) -> str:
        """Геттер, который выводит список товаров в виде строк"""
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str
