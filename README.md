# Overview

As a computer scientist, my overarching goal is to continuously expand my knowledge and skills in the field of computer science and leverage these competencies to contribute meaningfully to the world of technology. 

__How to Use the Program:__

* Upon launching the program, you are prompted to enter your username and password for authentication.
* After successful login, you have access to various features through a menu:

    * __Add Product:__ Allows you to input product details to add to your inventory.

    * __List Products:__ Displays a list of existing products in your inventory.

    * __Update Stock:__ Lets you increase the stock quantity for a particular product.

    * __Record Sale:__ Records a sale by specifying the product and quantity sold, updating stock accordingly.

    * __View Sales:__ Shows a history of sales, including the total quantity sold and total sales amount.

    * __Delete Product:__ Deletes a product from your inventory.

    * __Exit:__ Quits the program.

__Purpose of Writing the Software:__

The primary purpose of developing this software is to streamline the management of my small clothing brand business. By using this program, I aim to achieve the following objectives:

__Inventory Management:__ Effectively manage my product inventory by adding, updating, and deleting products as needed.

__Stock Control:__ Keep track of stock levels, allowing me to make informed decisions regarding reordering products.

__Sales Tracking:__ Record and monitor sales to understand which products are selling well and generate insights for business growth.

__Efficiency:__ Save time and reduce manual effort in managing business data by automating tasks through the software.

__Security:__ Implement user authentication to ensure that only authorized individuals can access and modify business data, enhancing data security.

This is a video showing how the program works:
[Software Demo Video](https://youtu.be/2AG2k9EL9QY)

# Cloud Database

I am using the Firebase Realtime Database, which is a cloud-hosted NoSQL database service provided by Google as part of the Firebase platform. Firebase

The database structure for this software consists of two main branches: "products" and "sales."

1. Products Branch: This branch stores information related to the products in my clothing brand's inventory. Each product is identified by a unique product ID. The structure within this branch includes:
    * __product_id:__ The unique identifier for each product.
    * __name:__ The name of the product.
    * __color:__ The color of the product.
    * __price:__ The price of the product.
    * __quantity:__ The current quantity of the product in stock.

2. Sales Branch: This branch records details of each sale transaction. Each sale entry includes:
    * __product_id:__ The ID of the product sold.
    * __quantity_sold:__ The quantity of the product sold in that transaction.
    * __date:__ The date when the sale was recorded.

The database structure is designed to facilitate efficient management of product inventory and the tracking of sales history. The "products" branch helps me keep tabs on product details and stock levels, while the "sales" branch records each sale, allowing for historical analysis and financial tracking.

# Development Environment

__Language:__ Python is the primary programming language used to develop this software. Python's versatility and extensive libraries make it a suitable choice for creating command-line applications.

__Firebase Admin SDK:__ I utilized the Firebase Admin SDK for Python to interact with the Firebase Realtime Database. This SDK provides the necessary functions to establish a connection with Firebase, read and write data, and manage user authentication.

__Operating System:__ The software was developed and tested on a macOS-based operating system. However, it's important to note that both Python and the Firebase SDK are cross-platform, ensuring compatibility with various operating systems, including macOS, Linux, and Windows. This cross-platform nature allows users to run the software on their preferred OS environment.

__Text Editor/IDE:__ Visual Studio Code (VS Code) was the chosen integrated development environment (IDE) for coding. VS Code is a popular and versatile code editor that provides extensive features and extensions for Python development and offers a seamless experience on macOS. 

__Version Control Systems:__ While the primary development and testing occurred within the VS Code IDE, __the terminal (command-line interface)__ was utilized for specific tasks, including Git version control operations. Additionally, I used __Sourcetree__, a graphical Git client, to manage and monitor Git repositories. These tools help ensure efficient version control, and the preservation of project progress.

# Useful Websites

- [Firestone Tutorial](https://firebase.google.com/docs/firestore)
- [Firebase Console](https://firebase.google.com/docs/firestore)

# Future Work

- Edit Products
- Record Sales with Previous Date
- Compute Profit in Addition to Total Sales
