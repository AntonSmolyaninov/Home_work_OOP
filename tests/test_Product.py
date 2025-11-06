import pytest

from src.Product import Product


def test_product_creation(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_create_product_with_default_quantity():
    """Тестируем создание продукта с использованием значения по умолчанию для quantity"""
    product_info = {
        'name': "iPhone 14",
        'description': "256GB, красный",
        'price': 80000.0
    }

    product = Product.new_product(product_info)

    assert product.name == "iPhone 14"
    assert product.description == "256GB, красный"
    assert product.price == 80000.0
    assert product.quantity == 0


def test_price_setter_and_getter():
    """Тестируем геттер и сеттер для цены"""
    product = Product("Nokia 3310", "Классический телефон", 5000.0, 10)

    assert product.price == 5000.0

    product.price = 6000.0
    assert product.price == 6000.0

    product.price = -1000.0
    assert product.price == 6000.0


def test_price_setter_prints_message_on_invalid_price(capfd):
    """Тестируем вывод сообщения при попытке установить неверную цену"""
    product = Product("Xiaomi Mi 11", "Флагманский смартфон", 50000.0, 3)
    product.price = -2000.0
    captured = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная." in captured.out
