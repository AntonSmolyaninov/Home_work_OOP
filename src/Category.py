class Category:
    name: str
    description: str
    product: list
    category_count = 0
    product_count = 0


    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product if product else []
        Category.category_count += 1
        Category.product_count += len(product) if product else 0

if __name__ == "__main__":
    category = Category("Овощи", "для салата", ["помидор", "огурец", "перец"])

    print(category.name)
    print(category.description)
    print(category.product)
    print(category.category_count)
    print(category.product_count)
