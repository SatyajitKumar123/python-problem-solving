"""
Problem:
Sort products by price (lowest to highest).

Approach:
Use sorted() with a key function that extracts the price from each dictionary.
The lambda function lambda x: x["price"] tells Python to sort by the price field.
"""


def sort_products(data):
    return sorted(data, key=lambda x: x["price"])

def sort_products_desc(data):
    return sorted(data, key=lambda x: x["price"], reverse=True)

if __name__=="__main__":
    
    products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 1500},
    ]
    
    print("Sorted")
    print(sort_products(products))
    
    print("\nDescenting order:")
    print(sort_products_desc(products))