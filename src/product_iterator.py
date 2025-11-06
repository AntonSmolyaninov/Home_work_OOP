
class ProductIterator:
    def __init__(self, products_obj):
        self.__products = products_obj
        self.index = 0

    def __iter__(self) -> 'ProductIterator':
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.__products):
            products = self.__products[self.index]
            self.index += 1
            return products
        else:
            raise StopIteration
