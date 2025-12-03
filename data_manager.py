import json
from models import Laptop, Accessory,Monitor


class DataManager:
    @staticmethod
    def save_inventory(filename, inventory):
        data = [item.to_dict() for item in inventory]
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print("Inventory saved successfully.")
        except IOError as e:
            print(f"Error saving file: {e}")

    @staticmethod
    def load_inventory(filename):
        inventory = []
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    if item['type'] == 'Laptop':
                        obj = Laptop(item['name'], item['sku'], item['price'], item['ram'])
                    elif item['type'] == 'Accessory':
                        obj = Accessory(item['name'], item['sku'], item['price'], item['compatibility'])
                    elif item['type'] == 'Monitor':
                        obj = Monitor(item['name'], item['sku'], item['price'], item['size'], item['resolution'])
                    else:
                        continue
                    inventory.append(obj)

        except FileNotFoundError:
            print("No previous data found. Starting fresh.")
        except json.JSONDecodeError:
            print("Data file corrupted. Starting fresh.")

        return inventory