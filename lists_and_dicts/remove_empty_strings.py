"""
Problem:
Remove empty strings and strings containing only whitespace from a list.

Approach:
1. Look at each item in the list one by one
2. Check if the item has any real content after removing leading/trailing whitespace
3. Keep only the items that contain actual text
4. Discard everything else (empty strings or strings that are just spaces)
"""

def clean_list(data):
    return [item for item in data if item.strip()]


if __name__ == "__main__":
    # Test cases
    test_lists = [
        ["hello", "", "python", " ", "backend"],        
        ["", " ", "\t", "\n"],                           
        ["apple", "banana", "cherry"],                   
        [],                                               
        ["  hello  ", "world", "", "  "],                 
    ]
    
    for lst in test_lists:
        result = clean_list(lst)
        print(f"Original: {lst}")
        print(f"Cleaned: {result}\n")