import pytest

from src.product import Product
from src.smartphone import Smartphone


def test_smartphone_initialization():
    smartphone = Smartphone(
        name="Test Phone",
        description="A test smartphone",
        price=699.99,
        quantity=10,
        efficiency=2.5,
        model="TP-2023",
        memory=128,
        color="Black",
    )

    assert smartphone.name == "Test Phone"
    assert smartphone.description == "A test smartphone"
    assert smartphone.price == 699.99
    assert smartphone.quantity == 10
    assert smartphone.efficiency == 2.5
    assert smartphone.model == "TP-2023"
    assert smartphone.memory == 128
    assert smartphone.color == "Black"


def test_smartphone_addition():
    smartphone1 = Smartphone("Phone1", "Desc1", 500, 2, 2.0, "ModelA", 64, "Blue")
    smartphone2 = Smartphone("Phone2", "Desc2", 700, 3, 3.0, "ModelB", 128, "Red")

    total_price_quantity = smartphone1 + smartphone2

    assert total_price_quantity == (500 * 2) + (700 * 3)


def test_smartphone_addition_type_error():
    smartphone = Smartphone("Phone1", "Desc1", 500, 2, 2.0, "ModelA", 64, "Blue")
    with pytest.raises(TypeError):
        _ = smartphone + "NotASmartphone"
