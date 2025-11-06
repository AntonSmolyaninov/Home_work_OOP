from src.Product import Product


class Category:
    name: str #название
    description: str #описание
    __products: list[Product]  # приватный атрибут, список товаров
    category_count: int = 0  # количество категорий
    product_count: int = 0  #количество товаров

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)


    def __str__(self):
        return f'{self.name}, количество продуктов: {Category.product_count} шт.'


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
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)} \n"

        return products_str
