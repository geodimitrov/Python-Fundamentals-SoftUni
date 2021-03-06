class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        filtered_products = []
        for product in self.products:
            if product.startswith(first_letter):
                filtered_products.append(product)
        return filtered_products

    def __repr__(self):
        return f"Items in the {self.name} catalogue:\n" + "\n".join([item for item in sorted(self.products)])

#Test Code
catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)