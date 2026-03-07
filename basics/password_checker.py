# Password strength checker

def check_password_strength(password):
    length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    score = sum([length, has_upper, has_lower, has_digit])

    print(f"Strength Score: {score}/4")

    if score == 4:
        print("Password is Strong!")
    elif score >= 2:
        print("Password is Moderate.")
    else:
        print("Password is Weak.")

        
if __name__=="__main__":
    pwd = input("Enter a password to check: ")
    check_password_strength(pwd)