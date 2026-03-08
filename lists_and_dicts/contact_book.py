# Simple Contact Book (Dictionary)
"""
Concept: Dictionaries, CRUD (Create, Read, Update, Delete).
Goal: Store names and phone numbers in a dictionary.
"""

contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print(f"Added {name}.")

def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name}.")
    else:
        print("Contact not found.")

def show_all():
    for name, number in contacts.items():
        print(f"{name}: {number}")

while True:
    action = input("\n(A)dd, (S)earch, (D)elete, (L)ist, (Q)uit: ").upper()
    if action == 'A':
        n = input("Name: ")
        p = input("Number: ")
        add_contact(n, p)
    elif action == 'S':
        search_contact(input("Name to search: "))
    elif action == 'D':
        delete_contact(input("Name to delete: "))
    elif action == 'L':
        show_all()
    elif action == 'Q':
        break
    
    
    