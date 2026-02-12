"""
Problem:
Check if two strings are anagrams.

Approach:
Two strings are anagrams if they have the same letters in the same quantity.

1. Sort both strings alphabetically
2. If the sorted versions are identical, they're anagrams

Example:
"listen" sorted -> "eilnst"
"silent" sorted -> "eilnst"
Both match -> True
"""

def check_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)


if __name__=="__main__":
    test_cases = [("listen", "silent"), ("race", "care"), ("trap", "part"), ("trap", "crap")]
    
    for i, j in test_cases:
        print(f"Is '{i}' and '{j}' anagram: {check_anagrams(i, j)}")