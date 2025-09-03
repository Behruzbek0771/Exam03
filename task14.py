class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def get_total(self):
        return sum(price for _, price in self.items)


cart = Cart()
cart.add_item("Laptop", 2000)
cart.add_item("Mouse", 100)
print(cart.get_total())
