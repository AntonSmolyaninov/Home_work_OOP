import pytest

from src.product import Product


def test_product_init():
    p = Product("One", "Test desc", 100.5, 2)
    assert p.name == "One"
    assert p.description == "Test desc"
    assert p.price == 100.5
    assert p.quantity == 2


def test_product_str():
    p = Product("One", "Test desc", 123.45, 7)
    s = str(p)
    assert "One" in s
    assert "123.45" in s
    assert "Остаток: 7" in s


def test_product_addition():
    p1 = Product("One", "Test desc", 10.0, 2)
    p2 = Product("Two", "Else", 5.0, 3)
    total = p1 + p2
    assert total == 35.0


def test_product_new_product_creates_new():
    products = []
    info = {"name": "Abc", "description": "Desc", "price": 77.0, "quantity": 3}
    p = Product.new_product(info, products)
    assert isinstance(p, Product)
    assert p.name == "Abc"
    assert p.quantity == 3


def test_product_new_product_updates_existing():
    products = [Product("Abc", "Desc", 77.0, 3)]
    info = {"name": "Abc", "description": "Desc2", "price": 88.0, "quantity": 2}
    existing = products[0]
    p = Product.new_product(info, products)
    assert p is existing
    assert p.quantity == 5  # 3 + 2
    assert p.price == 88.0


def test_product_price_setter():
    p = Product("Test", "Desc", 10.0, 1)
    p.price = 99.99
    assert p.price == 99.99
    with pytest.raises(ValueError):
        p.price = 0
    with pytest.raises(ValueError):
        p.price = -5


if __name__ == "__main__":
    pytest.main()
