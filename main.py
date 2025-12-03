from models import Laptop, Accessory, Monitor, Order
from data_manager import DataManager


def main():
    FILE_NAME = "inventory.json"

    manager = DataManager()

    inventory = manager.load_inventory(FILE_NAME)

    sales_totals = {"Laptop": 0.0, "Accessory": 0.0, "Monitor": 0.0}

    ADMIN_PASSWORD = "admin123"

    while True:
        print("\n--- TECH VAULT MEGA STORE ---")
        print("1. Add Laptop")
        print("2. Add Accessory")
        print("3. Add Monitor")
        print("4. Create Order (Buy Items)")
        print("5. View Sales Stats (PASSWORD REQUIRED)")
        print("6. Save & Exit")

        choice = input("Select option: ")

        try:
            # --- AGREGAR LAPTOP ---
            if choice == '1':
                name = input("Name: ")
                sku = input("SKU: ")
                price = float(input("Price: "))
                ram = int(input("RAM (GB): "))

                new_laptop = Laptop(name, sku, price, ram)
                inventory.append(new_laptop)
                print("Laptop added successfully.")

            # --- AGREGAR ACCESORIO ---
            elif choice == '2':
                name = input("Name: ")
                sku = input("SKU: ")
                price = float(input("Price: "))
                comp = input("Compatibility: ")

                new_acc = Accessory(name, sku, price, comp)
                inventory.append(new_acc)
                print(" Accessory added successfully.")

            # --- AGREGAR MONITOR---
            elif choice == '3':
                name = input("Name: ")
                sku = input("SKU: ")
                price = float(input("Price: "))
                size = float(input("Size (inches): "))
                res = input("Resolution (e.g. 4K, 1080p): ")

                new_monitor = Monitor(name, sku, price, size, res)
                inventory.append(new_monitor)
                print(" Monitor added successfully.")

            # --- CREAR ORDEN DE COMPRA ---
            elif choice == '4':
                if not inventory:
                    print(" Inventory is empty! Add products first.")
                    continue

                current_order = Order()

                while True:
                    print("\n--- INVENTORY LIST ---")
                    for idx, item in enumerate(inventory):
                        print(f"[{idx}] {item} - ({type(item).__name__})")

                    print("Enter index to add to cart (or 'x' to finish):")
                    pick = input("> ")

                    if pick.lower() == 'x':
                        break

                    # Validación de índice
                    if pick.isdigit() and 0 <= int(pick) < len(inventory):
                        selected_item = inventory[int(pick)]
                        current_order.add_product(selected_item)

                        # Actualizar diccionario de ventas
                        item_type = type(selected_item).__name__

                        # ERROR 2 FIX: Use .get_price() instead of .price
                        price_val = selected_item.get_price()

                        if item_type in sales_totals:
                            sales_totals[item_type] += price_val
                        else:
                            sales_totals[item_type] = price_val
                    else:
                        print(" Invalid index selection.")

                current_order.show_receipt()

            elif choice == '5':
                print("  SECURITY CHECK ")
                password = input("Enter Admin Password: ")

                if password == ADMIN_PASSWORD:
                    print("\n--- 🔒 SECRET SALES REPORT ---")
                    grand_total = 0
                    for category, total in sales_totals.items():
                        print(f" {category}: ${total:.2f}")
                        grand_total += total
                    print("--------------------------")
                    print(f"GROSS REVENUE: ${grand_total:.2f}")
                else:
                    print(" ACCESS DENIED. Incorrect Password.")

            # --- GUARDAR Y SALIR ---
            elif choice == '6':
                # ERROR 1 FIX: Use the instance 'manager' to save
                manager.save_inventory(FILE_NAME, inventory)
                print(" System Saved. Goodbye!")
                break

        except ValueError:
            print("Error: Please enter a valid number for Price/RAM/Size.")
        except Exception as e:
            print(f" Unexpected Error: {e}")
        finally:
            print("-" * 30)


if __name__ == "__main__":
    main()