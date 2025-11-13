import pytest

from src.lawngrass import LawnGrass
from src.product import Product


def test_lawn_grass_initialization():
    lawn_grass = LawnGrass(
        name="Green Lawn",
        description="Premium grass for lawns",
        price=29.99,
        quantity=5,
        country="USA",
        germination_period="7 days",
        color="Green",
    )

    assert lawn_grass.name == "Green Lawn"
    assert lawn_grass.description == "Premium grass for lawns"
    assert lawn_grass.price == 29.99
    assert lawn_grass.quantity == 5
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "7 days"
    assert lawn_grass.color == "Green"


def test_lawn_grass_addition():
    lawn_grass1 = LawnGrass("Grass1", "Desc1", 20.0, 10, "USA", "10 days", "Dark Green")
    lawn_grass2 = LawnGrass("Grass2", "Desc2", 15.0, 8, "Canada", "12 days", "Light Green")

    total_price_quantity = lawn_grass1 + lawn_grass2

    assert total_price_quantity == (20.0 * 10) + (15.0 * 8)


def test_lawn_grass_addition_type_error():
    lawn_grass = LawnGrass("Grass1", "Desc1", 20.0, 10, "USA", "10 days", "Dark Green")
    with pytest.raises(TypeError):
        _ = lawn_grass + "NotALawnGrass"
