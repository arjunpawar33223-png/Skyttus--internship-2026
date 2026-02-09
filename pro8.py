class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, discount_percent):
        discount_amount = self.price * discount_percent / 100
        self.price -= discount_amount
        print(f"Price after {discount_percent}% discount: {self.price}")

# Example
laptop = Laptop("Dell", 50000)
laptop.apply_discount(10)