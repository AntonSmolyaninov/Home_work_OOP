import pytest

from src.Category import Category
from src.Product import Product


def test_category_init(category, product1, product2):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"
    # Проверяем, что оба продукта есть в результатах products (т.к. это общий текст)
    assert product1.name in category.products
    assert product2.name in category.products


def test_category_str(category):
    s = str(category)
    assert "Смартфоны" in s
    assert "количество продуктов" in s


def test_category_products_returns_string(category):
    result = category.products
    assert isinstance(result, str)
    # Должен содержать оба продукта
    assert "Samsung" in result and "Iphone" in result


def test_add_product(category):
    old_products_str = category.products
    new_product = Product("Pixel", "Google phone", 50000.0, 2)
    category.add_product(new_product)
    assert "Pixel" in category.products
    assert category.products.count("Pixel") == 1


def test_category_counters_are_class_vars():
    old_cc = Category.category_count
    old_pc = Category.product_count
    p1 = Product("AA", "D", 1, 1)
    p2 = Product("BB", "E", 2, 2)
    c = Category("Test", "desc", [p1, p2])
    assert Category.category_count == old_cc + 1
    assert Category.product_count == old_pc + 2


def test_add_product_increases_product_count(category):
    main_count = Category.product_count
    new_prod = Product("X", "D", 1, 1)
    category.add_product(new_prod)
    assert Category.product_count == main_count + 1


if __name__ == "__main__":
    pytest.main()
