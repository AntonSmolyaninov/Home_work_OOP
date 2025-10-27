import json
import os

from src.Product import Product
from src.Category import Category


def load_categories_from_json(filepath: str):
    """Загружает категории и продукты из файла JSON по указанному пути."""
    absolute_path = os.path.abspath(filepath)

    with open(absolute_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        categories = []
        for item in data:
            product_list = [
                Product(prod['name'], prod['description'], prod['price'], prod['quantity'])
                for prod in item['products']
            ]
            category = Category(item['name'], item['description'], product_list)
            categories.append(category)
        return categories