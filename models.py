class Product:
    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        # Use the setter method to ensure validation runs on creation
        self.set_price(price)

    # REPLACED @property with standard get_price method
    def get_price(self):
        return self._price

    # REPLACED @price.setter with standard set_price method
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    def to_dict(self):
        raise NotImplementedError("Subclasses must implement to_dict")

    def __str__(self):
        # Updated to use get_price()
        return f"{self.name} (${self.get_price():.2f})"


class Laptop(Product):
    def __init__(self, name, sku, price, ram):
        super().__init__(name, sku, price)
        self.ram = ram

    def to_dict(self):
        return {
            "type": "Laptop",
            "name": self.name,
            "sku": self.sku,
            "price": self.get_price(), # Updated
            "ram": self.ram
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
            "price": self.get_price(), # Updated
            "compatibility": self.compatibility
        }


class Monitor(Product):
    def __init__(self, name, sku, price, size, resolution):
        super().__init__(name, sku, price)
        self.size = size
        self.resolution = resolution

    def to_dict(self):
        return {
            "type": "Monitor",
            "name": self.name,
            "sku": self.sku,
            "price": self.get_price(), # Updated
            "size": self.size,
            "resolution": self.resolution
        }


class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            print(f"Added {product.name} to cart.")
        else:
            print("Invalid item.")

    def calculate_total(self):
        total = 0
        for p in self.products:
            # Updated to use get_price()
            total += p.get_price()
        return total

    def show_receipt(self):
        print("\n--- Receipt ---")
        for p in self.products:
            # Updated to use get_price()
            print(f"- {p.name}: ${p.get_price():.2f}")
        print(f"Total: ${self.calculate_total():.2f}")
        print("----------------")