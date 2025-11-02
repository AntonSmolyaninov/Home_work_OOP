from src.Product import Product


class Category:
    # Статические счетчики для всех экземпляров
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = name
        self.description = description
        self._products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self._products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в список товаров"""
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для возвращения строкового представления всех продуктов"""
        if not self._products:
            return "Нет продуктов в категории"

        return "\n".join(
            f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.' for product in self._products)
