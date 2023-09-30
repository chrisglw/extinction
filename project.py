from firebase_admin import initialize_app, credentials, db
import os
import datetime

# Initialize Firebase Admin with your private key
cred = credentials.Certificate("extinction-credentials.json")
initialize_app(cred, {'databaseURL': 'https://extinction-44ff5-default-rtdb.firebaseio.com/'})

def clear():
    os.system("clear")

# Reference to the Firebase Realtime Database
ref = db.reference()

def add_product():
    while True:
        product_id = input("Enter product ID (or 'q' to quit): ")
        if product_id.lower() == 'q':
            break
        name = input("Enter product name: ")
        color = input("Enter product color: ")
        design = input("Enter product design: ")
        quantity = int(input("Enter initial quantity: "))
        
        product_data = {
            "name": name,
            "color": color,
            "design": design,
            "quantity": quantity
        }
        ref.child("products").child(product_id).set(product_data)
        
        print("Product added successfully.")

def list_products():
    products = ref.child("products").get()
    if products:
        for product_id, product_data in products.items():
            print(f"Product ID: {product_id}")
            print(f"Name: {product_data.get('name')}")
            print(f"Color: {product_data.get('color')}")
            print(f"Design: {product_data.get('design')}")
            print(f"Quantity in Stock: {product_data.get('quantity')}")
            print("-" * 30)
        
        input("Enter any key to go back to the main menu.")
    else:
        print("There are not products yet.")

def update_stock():
    while True:
        list_products()
        product_id = input("Enter the product ID to update stock: ")
        quantity_to_add = int(input("Enter the quantity to add: "))
        
        product_ref = ref.child("products").child(product_id)
        product_data = product_ref.get()
        
        if product_data:
            current_quantity = product_data.get('quantity', 0)
            new_quantity = current_quantity + quantity_to_add
            product_ref.update({"quantity": new_quantity})
            print("Stock updated successfully.")
        else:
            print("Product not found.")
        
        choice = input("Do you want to update another product's stock? (yes/no): ")
        if choice.lower() != "yes":
            break

def record_sale():
    while True:
        list_products()
        product_id = input('Enter the product ID for the sale (or press "q" to quit): ')
        if product_id.lower() == 'q':
            break
        quantity_sold = int(input("Enter the quantity sold: "))
        
        product_ref = ref.child("products").child(product_id)
        product_data = product_ref.get()
        
        if product_data:
            current_quantity = product_data.get('quantity', 0)
            if current_quantity >= quantity_sold:
                current_date = datetime.date.today().strftime("%Y-%m-%d")
                sale_data = {
                    "product_id": product_id,
                    "quantity_sold": quantity_sold,
                    "date": current_date
                }
                ref.child("sales").push(sale_data)
                product_ref.update({"quantity": current_quantity - quantity_sold})
                print("Sale recorded successfully.")
            else:
                print("Insufficient stock for the sale.")
        else:
            print("Product not found.")


def view_sales():
    sales = ref.child("sales").get()
    if sales:
        total_sales_quantity = 0
        total_sales_amount = 0.0
        print("Sales History:")
        for sale_id, sale_data in sales.items():
            product_id = sale_data.get('product_id', 'N/A')
            quantity_sold = sale_data.get('quantity_sold', 0)
            
            # Retrieve product data to calculate the total amount for this sale
            product_ref = ref.child("products").child(product_id)
            product_data = product_ref.get()
            if product_data:
                product_price = product_data.get('price', 0.0)
                sale_amount = product_price * quantity_sold
                total_sales_amount += sale_amount
            
            total_sales_quantity += quantity_sold
            print(f"Product ID: {product_id} - Quantity Sold: {quantity_sold}")
        
        print(f"Total Sales Quantity: {total_sales_quantity}")
        print(f"Total Sales Amount: ${total_sales_amount:.2f}")
        
        input("Press Enter to go back to the main menu...")
    else:
        print("No sales recorded yet.")


while True:
    print("\nWelcome to Extinction App")
    print("1. Add Product")
    print("2. List Products")
    print("3. Update Stock")
    print("4. Record Sale")
    print("5. View Sales")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        list_products()

    elif choice == "3":
        update_stock()

    elif choice == "4":
        record_sale()

    elif choice == "5":
        view_sales()

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.") 