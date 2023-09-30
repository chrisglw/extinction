from firebase_admin import initialize_app, credentials, db
import os
import datetime
import time

# Initialize Firebase Admin with your private key
cred = credentials.Certificate("extinction-credentials.json")
initialize_app(cred, {'databaseURL': 'https://extinction-44ff5-default-rtdb.firebaseio.com/'})

#clears terminal
def clear():
    os.system("clear")

# Reference to the Firebase Realtime Database
ref = db.reference()

# Function to add a product
def add_product():
    while True:
        product_id = input("Enter product ID (or 'q' to quit): ")
        if product_id.lower() == 'q':
            break
        
        name = input("Enter product name: ")
        color = input("Enter product color: ")
        price = float(input("Enter product price: ")) 
        quantity = int(input("Enter initial quantity: "))
        
        product_data = {
            "name": name,
            "color": color,
            "price": price, 
            "quantity": quantity
        }
        ref.child("products").child(product_id).set(product_data)
        
        print("Product added successfully.")

# Function to display a list of products
def list_products(show_back_message=True):
    clear()
    products = ref.child("products").get()
    if products:
        for product_id, product_data in products.items():
            print(f"Product ID: {product_id}")
            print(f"Name: {product_data.get('name')}")
            print(f"Color: {product_data.get('color')}")
            print(f"Quantity in Stock: {product_data.get('quantity')}")
            print("-" * 30)
        
        if show_back_message:
            input("Enter any key to go back to the main menu.")
    else:
        print("There are no products yet.")
        time.sleep(2)
        return

# Function to add more pieces to current stock 
def update_stock():
    while True:
        list_products(show_back_message=False)
        products = ref.child("products").get()
        if not products:
            return
        
        product_id = input("Enter the product ID to update stock (or 'q' to quit): ")  
        if product_id.lower() == 'q':
            break

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
    return

# Function to process a sale
def record_sale():
    clear()
    products = ref.child("products").get()
    if not products:
        print("There are no products yet.")
        time.sleep(2)
        return
    
    while True:
        list_products(show_back_message=False)
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

# Function to show all the sales and the total money amount
def view_sales():
    clear()
    products = ref.child("products").get()
    if not products:
        print("There are no products yet.")
        time.sleep(2)
        return
    
    sales = ref.child("sales").get()
    if sales:
        total_sales_quantity = 0
        total_sales_amount = 0.0
        print("Sales History:")
        for sale_id, sale_data in sales.items():
            product_id = sale_data.get('product_id', 'N/A')
            quantity_sold = sale_data.get('quantity_sold', 0)
            
            # Retrieve product data including price to calculate the total amount for this sale
            product_ref = ref.child("products").child(product_id)
            product_data = product_ref.get()
            if product_data:
                product_price = product_data.get('price', 0.0)
                sale_amount = product_price * quantity_sold
                total_sales_amount += sale_amount
            
            total_sales_quantity += quantity_sold
            print(f"Product ID: {product_id} - Quantity Sold: {quantity_sold} - Sale Amount: ${sale_amount:.2f}")  # Display sale amount for each sale
        
        print(f"Total Sales Quantity: {total_sales_quantity}")
        print(f"Total Sales Amount: ${total_sales_amount:.2f}")
        
        input("Press Enter to go back to the main menu.")
    else:
        print("No sales recorded yet.")
        time.sleep(2) 
        return 

# Function to delete a product 
def delete_product():
    clear()
    products = ref.child("products").get()
    if not products:
        print("There are no products yet.")
        time.sleep(2)
        return
    
    while True:
        list_products(show_back_message=False)
        product_id = input('Enter the product ID to delete (or press "q" to quit): ')
        if product_id.lower() == 'q':
            break
        
        product_ref = ref.child("products").child(product_id)
        product_data = product_ref.get()
        
        if product_data:
            product_name = product_data.get('name', 'N/A')
            confirmation = input(f"Are you sure you want to delete '{product_name}'? (yes/no): ")
            if confirmation.lower() == 'yes':
                product_ref.delete()
                print(f"'{product_name}' has been deleted.")
            else:
                print(f"'{product_name}' was not deleted.")
        else:
            print("Product not found.")

while True:
    clear()
    print("\nWelcome to Extinction App")
    print("1. Add Product")
    print("2. List Products")
    print("3. Update Stock")
    print("4. Record Sale")
    print("5. View Sales")
    print("6. Delete Product")
    print("7. Exit")

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
        delete_product()
    elif choice == "7":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")