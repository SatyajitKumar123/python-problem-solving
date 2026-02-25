"""
Problem:
Convert a list of strings to integers, safely ignoring any strings that can't be converted.

Approach:
1. Look at each item in the list one by one
2. Try to convert it to an integer
3. If successful -> add it to our result list
4. If conversion fails (ValueError) -> skip it and move to next item
5. Continue until all items are processed
"""

def safe_convert(data):
    result = []
    for item in data:
        try:
            result.append(int(item))
        except ValueError:
            pass
    return result


if __name__=="__main__":
    test_lists = [
        ["10", "20", "abc", "30"],              
        ["1", "2", "3", "4", "5"],               
        ["abc", "def", "ghi"],                   
        [],                                        
        ["-5", "0", "42", "3.14", "100"],         
        ["  10  ", "20", " 30 "],
        ["", " ", "\t"], 
    ]
    
    for i, lst in enumerate(test_lists, 1):
        result = safe_convert(lst)
        print(f"Test {i}:")
        print(f"  Original: {lst}")
        print(f"  Converted: {result}")
        print()