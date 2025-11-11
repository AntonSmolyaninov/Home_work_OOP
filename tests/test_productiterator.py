import pytest

from src.Product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def products_list():
    return [
        Product("A", "Desc A", 10.0, 1),
        Product("B", "Desc B", 20.0, 3),
        Product("C", "Desc C", 30.0, 4),
    ]


def test_iterator_returns_all_products(products_list):
    it = ProductIterator(products_list)
    collected = [p for p in it]
    assert len(collected) == len(products_list)
    for i, p in enumerate(products_list):
        assert collected[i].name == p.name
        assert collected[i].price == p.price


def test_iterator_is_iterable(products_list):
    it1 = ProductIterator(products_list)
    it2 = iter(it1)
    assert it1 is it2  # __iter__ всегда возвращает self
    next(it2)  # после вызова next объект не сломался
    assert hasattr(it2, "__next__")


def test_iterator_stops(products_list):
    it = ProductIterator(products_list)
    for _ in products_list:
        next(it)
    with pytest.raises(StopIteration):
        next(it)


def test_iterator_reset(products_list):
    it = ProductIterator(products_list)
    names1 = [p.name for p in it]
    names2 = [p.name for p in it]  # итератор должен сбрасывать индекс, как реализовано
    assert names1 == names2


def test_iterator_with_empty_list():
    it = ProductIterator([])
    with pytest.raises(StopIteration):
        next(it)


if __name__ == "__main__":
    pytest.main()
