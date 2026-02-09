"""
Problem:
Reverse a string without using slicing.

Approach:
Iterate through each character and build the reversed string manually.
"""

def reverse_string(s: str) -> str:
    result = ""
    for ch in s:
        result = ch + result
    return result

if __name__=="__main__":
    
    test_cases = ["satyajit", "hello", "world", "python"]
    for word in test_cases:
        print(f"{word}: {reverse_string(word)}")