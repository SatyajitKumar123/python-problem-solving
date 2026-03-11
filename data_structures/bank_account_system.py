# Bank Account System (OOP Basics)
"""
Concept: Classes, Objects, Attributes, Methods, Encapsulation.
Goal: Model a real-world object using a Class.
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        
    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}.")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance
    
def main():
    acc = BankAccount("Satyajit", 1000)
    print(f"Owner: {acc.owner}")

    acc.deposite(500)
    acc.withdraw(300)
    print(f"Current Balance: ₹{acc.get_balance()}")
    
if __name__=="__main__":
    main()