# Inventory System (OOP)
"""
Real-World Use: E-commerce backends need to track stock levels safely.
"""

class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity
        
    def sell(self, amount):
        if amount > self.__quantity:
            return False, "Insufficient stock"
        self.__quantity -= amount
        return True, "Sale successful"

    def restock(self, amount):
        self.__quantity += amount
        
    def get_quantity(self):
        return self.__quantity
    

# test
def run_tests():
    item = InventoryItem("Laptop", 1000, 5)

    assert item.get_quantity() == 5
    
    # sell successfully
    success, msg = item.sell(2)
    assert success is True
    assert item.get_quantity() == 3
    
    # sell fail
    success, msg = item.sell(10)
    assert success is False
    
    # restock
    item.restock(10)
    assert item.get_quantity() == 13
    
    print("All inventory_system tests passed.")
    
if __name__=="__main__":
    run_tests()