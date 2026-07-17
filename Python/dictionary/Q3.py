"construct a dictionary containing 4 product names & their prices"
"prompt the user to enter a product name"
"use the in keyword to check if it exists"
"if so display its prize otherwise inform the user product not found"

products = {"mobile": 23000,
            "earphone": 10000,
            "smartwatch": 2000,
            "laptop": 70000
            }
product = input("enter product name")
if product in products:
    print(f" product name: {product}, its price {products[product]}")
else:
    print(f"product not found")