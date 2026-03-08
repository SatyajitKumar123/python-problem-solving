# Input Valitor(Error Handling)
"""
Concept: Try/Except Blocks, Custom Exceptions.
Goal: Force the user to provide valid data, handling crashes gracefully.
"""

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Number must be positive")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

def safe_division():
    print("--- Safe Division ---")
    num1 = get_positive_int("Enter numerator: ")
    num2 = get_positive_int("Enter dominator: ")

    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"Result: {result}")
    finally:
        print("Operation finished.")

if __name__=="__main__":
    safe_division()