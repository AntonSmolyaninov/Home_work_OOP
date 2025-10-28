import json
from unittest.mock import mock_open, patch

from src.utils import load_categories_from_json

mock_json_data = """
[
    {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000,
                "quantity": 5
            },
            {
                "name": "Iphone 15",
                "description": "512GB, Gray space",
                "price": 210000,
                "quantity": 8
            },
            {
                "name": "Xiaomi Redmi Note 11",
                "description": "1024GB, Синий",
                "price": 31000,
                "quantity": 14
            }
        ]
    },
    {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        "products": [
            {
                "name": "55\\\" QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000,
                "quantity": 7
            }
        ]
    }
]
"""


@patch("builtins.open", new_callable=mock_open, read_data=mock_json_data)
def test_load_categories_from_json(mock_file):
    filepath = "mock_file.json"

    result = load_categories_from_json(filepath)

    # Проверяем, что результат содержит правильные данные
    assert len(result) == 2
    assert result[0].name == "Смартфоны"
    assert (
        result[0].description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(result[0].products) == 3
    assert result[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert result[0].products[1].name == "Iphone 15"
    assert result[0].products[2].name == "Xiaomi Redmi Note 11"

    assert result[1].name == "Телевизоры"
    assert (
        result[1].description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(result[1].products) == 1
    assert result[1].products[0].name == '55" QLED 4K'
