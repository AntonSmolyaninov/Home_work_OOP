class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)


if __name__ == "__main__":
    category = Category("Овощи", "для салата", ["помидор", "огурец", "перец"])

    print(category.name)
    print(category.description)
    print(category.products)
    print(Category.category_count)
    print(Category.product_count)
