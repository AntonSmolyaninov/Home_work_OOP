import json
import os

from src.category import Category
from src.product import Product


def load_categories_from_json(filepath: str) -> list[Category]:
    """Загружает категории и продукты из файла JSON по указанному пути.
    :rtype: list[Category]
    """
    absolute_path = os.path.abspath(filepath)

    with open(absolute_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        categories = []
        for item in data:
            product_list = [
                Product(prod["name"], prod["description"], prod["price"], prod["quantity"])
                for prod in item["products"]
            ]
            category = Category(item["name"], item["description"], product_list)
            categories.append(category)
        return categories
