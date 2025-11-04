from src.Category import Category
from src.Product import Product

def test_category_initialization(category):
    """Тестируем инициализацию категории"""
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"
    assert len(category.in_products) == 2  # Должно быть 2 продукта в категории


def test_add_new_product_to_category(category):
    """Тестируем добавление нового продукта в категорию"""
    new_product = Product("Xiaomi Redmi Note 11", "128GB, Черный", 31000.0, 10)
    category.add_product(new_product)

    assert len(category.in_products) == 3  # Теперь должно быть 3 продукта
    assert category.in_products[2].name == "Xiaomi Redmi Note 11"


def test_add_existing_product_updates_quantity(category):
    """Тестируем добавление существующего продукта с обновлением количества"""
    existing_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 3)
    category.add_product(existing_product)

    # Количество первого продукта должно обновиться
    assert category.in_products[0].quantity == 8  # 5 + 3


def test_add_existing_product_updates_price(category):
    """Тестируем добавление существующего продукта с обновлением цены"""
    higher_price_product = Product("Iphone 15", "512GB, Gray space", 250000.0, 2)
    category.add_product(higher_price_product)

    # Цена второго продукта должна обновиться
    assert category.in_products[1].price == 250000.0  # Должна быть новая более высокая цена

