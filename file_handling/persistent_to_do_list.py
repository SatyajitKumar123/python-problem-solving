# Persistent To-Do List (File I/O)
"""
Concept: Reading/Writing Files, Context Managers (with).
Goal: Save tasks to a text file so they remain after the script closes.
"""

import os 

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return f.read().splitlines()
    
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View 2. Add 3. Remove 4. Exit")
        choice = input("Choice: ")

        if choice == '1':
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '2':
            task = input("New task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == '3':
            try:
                idx = int(input("Task number to remove: ")) - 1
                tasks.pop(idx)
                save_tasks(tasks)
            except (IndexError, ValueError):
                print("Invalid number.")
        elif choice == '4':
            break

if __name__=="__main__":
    main()