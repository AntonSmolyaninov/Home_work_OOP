from src.Product import Product


class Category:
    name: str
    description: str
    __products: list[Product]  # Приватный атрибут, содержащий продукты
    category_count: int = 0  # Общее количество категорий
    product_count: int = 0  # Общее количество продуктов во всех категориях

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в список товаров"""
        found = False

        for existing_product in self.__products:
            if existing_product.name == product.name:
                # Если продукт с таким именем уже существует, обновляем quantity и price при необходимости
                existing_product.quantity += product.quantity  # Увеличиваем количество на количество продукта
                if product.price > existing_product.price:
                    existing_product.price = product.price  # Устанавливаем более высокую цену
                found = True
                break

        if not found:
            self.__products.append(product)
            Category.product_count += 1  # Увеличиваем глобальный счетчик

    @property
    def products(self) -> str:
        """Геттер, который выводит список товаров в виде строк"""
        if not self.__products:
            return "Нет продуктов в категории"

        return "\n".join(
            f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.' for product in self.__products
        )
