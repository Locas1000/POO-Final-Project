class Product:
    def __init__(self,name,sku,price):
        self.name=name
        self.sku=sku
        self._price=price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError("price can't be negative.")
        self._price = value

    def to_dict(self):
        pass

    def __str__(self):
        return f"{self.name} (${self.price})"

class Laptop(Product):
    def __init__(self,name,sku,price,ram):
        super().__init__(name,sku,price)
        self.ram=ram

    def to_dict(self):
        return {
            "type": "Laptop",
            "name": self.name,
            "sku": self.sku,
            "price": self.price,
            "ram": self.ram,
        }

class Accessory(Product):
    def __init__(self, name, sku, price, compatibility):
        super().__init__(name, sku, price)
        self.compatibility = compatibility

    def to_dict(self):
        return {
            "type": "Accessory",
            "name": self.name,
            "sku": self.sku,
            "price": self.price,
            "compatibility": self.compatibility
        }


class Order:
    def __init__(self):
        self.products = []  # Composition (List of Objects)

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            print(f"Added {product.name} to cart.")
        else:
            print("Invalid item.")

    def calculate_total(self):
        total = 0
        for p in self.products:
            total += p.price
        return total

    def show_receipt(self):
        print("\n--- Receipt ---")
        for p in self.products:
            print(f"- {p.name}: ${p.price:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")
        print("----------------")