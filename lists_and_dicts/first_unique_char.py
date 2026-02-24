"""
Problem:
Return the first character that does not repeat in a string.

Example:
"swiss"

Output:
"w"

Approach:
Think of it like taking attendance twice:

Pass 1 (Counting): Go through the string and count how many times each character appears.
                   Store counts in a dictionary (like a tally sheet).

Pass 2 (Finding): Go through the string again in order.
                  For each character, check its count.
                  The first character with count = 1 is our answer!
"""

from collections import Counter

def first_unique_char(s):
    count = Counter(s)
    
    for char in s:
        if count[char] == 1:
            return char
        
    return None


if __name__ == "__main__":
    test_cases = [
        "leetcode",
        "loveleetcode",
        "aabb",               
        "a",
        "abab",               
        "swiss",
        "",                   
    ]
    
    for s in test_cases:
        result = first_unique_char(s)
        print(f"'{s}' → first unique char: {result}")