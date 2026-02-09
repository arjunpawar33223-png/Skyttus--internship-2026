class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product} added to the shop.")

    def list_products(self):
        print("Products in shop:")
        for p in self.products:
            print("-", p)

# Example
shop = Shop()
shop.add_product("Laptop")
shop.add_product("Mouse")
shop.list_products()