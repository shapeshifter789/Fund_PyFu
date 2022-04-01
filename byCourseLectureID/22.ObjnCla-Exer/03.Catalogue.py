class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = list()

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        get_by_letter_list = [product for product in self.products if product[0] == first_letter]
        return get_by_letter_list

    def __repr__(self):
        new_line = '\n'
        return f"Items in the {self.name} catalogue:\n{new_line.join(sorted(self.products))}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
