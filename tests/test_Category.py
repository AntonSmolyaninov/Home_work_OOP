from src.Category import Category


def test_category_creation(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"
    assert len(category.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2
