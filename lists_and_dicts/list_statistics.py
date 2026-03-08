# List Statistics Calculator
"""
Concept: Lists, Loops, Built-in Functions.
Goal: Accept a series of numbers from a user and calculate stats.
"""

def calculate_stats():
    numbers = []
    print("Enter numbers one by one. Type 'done' to finish.")

    while True:
        user_input = input("Enter number: ")
        if user_input.lower() == 'done':
            break
        try:
            numbers.append(float(user_input))
        except ValueError:
            print("Invalid input.")

    if not numbers:
        print("No numbers entered.")
        return 
    
    print(f"\nList: {numbers}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.2f}")
    print(f"Max: {max(numbers)}")
    print(f"Min: {min(numbers)}")
    

if __name__=="__main__":
    calculate_stats()