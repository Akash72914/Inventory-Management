inventory = {}

sales = []

def add_product():
    """
    Adds a new product to the inventory.
    Ensures product ID is unique before adding.
    """
    product_id = input("Enter Product ID: ")
    if product_id in inventory:
        print("Product ID already exists. Please enter a unique ID.")
        return
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    quantity = int(input("Enter Product Quantity: "))
    inventory[product_id] = {'name': name, 'price': price, 'quantity': quantity}
    print("Product added successfully.")

def view_inventory():
    """
    Displays all products in the inventory in a tabular format.
    """
    print("\nInventory:")
    print("{:<10} {:<15} {:<10} {:<10}".format("ID", "Name", "Price", "Quantity"))
    for pid, details in inventory.items():
        print("{:<10} {:<15} {:<10} {:<10}".format(pid, details['name'], details['price'], details['quantity']))

def sell_product():
    """
    Processes the sale of a product.
    Checks for product availability and sufficient stock before selling.
    Updates the inventory and records the sale in sales list.
    """
    product_id = input("Enter Product ID to sell: ")
    if product_id not in inventory:
        print("Product not found.")
        return
    quantity_sold = int(input("Enter Quantity to sell: "))
    if quantity_sold > inventory[product_id]['quantity']:
        print("Insufficient stock available.")
        return
    inventory[product_id]['quantity'] -= quantity_sold
    sales.append({'product_id': product_id, 'quantity': quantity_sold, 'total_price': quantity_sold * inventory[product_id]['price']})
    print("Product sold successfully.")

def restock_product():
    """
    Adds stock to an existing product in the inventory.
    Displays error if product does not exist.
    """
    product_id = input("Enter Product ID to restock: ")
    if product_id not in inventory:
        print("Product not found.")
        return
    quantity_added = int(input("Enter Quantity to add: "))
    inventory[product_id]['quantity'] += quantity_added
    print("Product restocked successfully.")

def generate_sales_report():
    """
    Generates and displays the sales report including
    total items sold and total revenue.
    """
    total_items_sold = sum(sale['quantity'] for sale in sales)
    total_revenue = sum(sale['total_price'] for sale in sales)
    print("\nSales Report:")
    print(f"Total Items Sold: {total_items_sold}")
    print(f"Total Revenue: ₹{total_revenue}")

def main():
    """
    Main function providing a menu-based interface to the user
    for managing inventory operations.
    """
    while True:
        print("\n--- Inventory Management Menu ---")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Sell Product")
        print("4. Restock Product")
        print("5. Generate Sales Report")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            sell_product()
        elif choice == '4':
            restock_product()
        elif choice == '5':
            generate_sales_report()
        elif choice == '6':
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Please select between 1-6.")

# Entry point of the program
if __name__ == "__main__":
    main()
