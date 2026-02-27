"""
Problem:
Validate that a dictionary (user data) contains all required fields.
Example: {"name": "Satyajit", "email": "test@mail.com"} -> True (has both name and email)
Example: {"name": "Satyajit"} -> False (missing email)

Approach:
Think of it like checking a form before submitting:

1. You have a list of required fields (like a checklist)
2. You have a dictionary of user-provided data
3. Go through each required field and check:
   - Is this field present in the user's data?
4. If ANY required field is missing -> validation fails (return False)
5. If ALL required fields are present -> validation passes (return True)
"""

def validate_user(data):
    required = ["name", "email"]
    for field in required:
        if field not in data or not data[field]:
            return False
    return True

if __name__ == "__main__":
    
    test_data = [
        {"name": "Satyajit", "email": "test@mail.com"},      
        {"name": "Satyajit"},                                  
        {"email": "test@mail.com"},                            
        {},                                                     
        {"name": "", "email": "test@mail.com"},                
        {"name": "Satyajit", "email": "", "age": 30},          
        {"name": "Satyajit", "email": "test@mail.com", "age": 30},   
    ]
    
    for i, data in enumerate(test_data, 1):
        is_valid = validate_user(data)

        print(f"Test {i}: {data}")
        print(f"  Basic validation: {is_valid}")
        