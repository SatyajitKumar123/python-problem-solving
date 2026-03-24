# Secure Password Generator

"""
Real-World Use: Creating strong credentials for users or databases.
"""

import random 
import string

def generate_password(length=12):
    """
    Generates a password with uppercase, lowercase, digits, and symbols.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4")
    
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)
    
    return "".join(password)



if __name__=="__main__":
    pwd = generate_password(8)
    print(pwd)