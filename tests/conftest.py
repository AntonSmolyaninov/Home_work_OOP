import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category(product1, product2):
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации", [product1, product2])
