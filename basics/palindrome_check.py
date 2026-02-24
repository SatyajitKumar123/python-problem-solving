"""
Problem:
Check if a string is a palindrome (reads same forwards and backwards),
ignoring spaces, punctuation, and case.

Approach:
Think of it like cleaning a messy sentence before checking if it reads the same backwards:

Step 1 (Clean): Remove everything that's not a letter or number (spaces, punctuation, etc.)
                Convert everything to lowercase so 'A' and 'a' match.

Step 2 (Compare): Check if the cleaned string equals its reverse.
                  If yes → palindrome! If no → not a palindrome.
"""

import re

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]


if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",  
        "race a car",                       
        " ",
        "racecar",                           
        "hello",                             
        "Madam",                             
        "12321",                             
        "No 'x' in Nixon",                   
        "Was it a car or a cat I saw?",       
    ]
    
    for s in test_cases:
        result = is_palindrome(s)
        print(f"'{s}' -> Palindrome: {result}")