#ya acabe
import json
from models import Laptop, Accessory

class DataManager:
    @staticmethod

    def save_data(filename, inventory):
        data = [item.to_dict() for item in inventory]
        try:
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
            print("Data saved")

            for item in data:
                if item['type'] == 'Laptop':
                    obj = Laptop(item['name'], item['sku'], item['price'], item['ram'])
                elif item['type'] == 'Accessory':
                    obj = Accessory(item['name'], item['sku'], item['price'], item['conpatibility'])
                else:
                    continue
                inventory.append(obj)
        except IOError:
            print("Could not save data")
    def load_data(self):
        inventory = []
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            print("Could not load data")
        except json.JSONDecodeError:
            print("Data file corrupted. Starting fresh.")
        return inventory