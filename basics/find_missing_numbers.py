"""
Problem:
Find the missing number from 1 to n.

Approach:
This solution uses sets to find what's missing

1. Create a set with all numbers from 1 to n
2. Convert the input list into another set
3. Subtract the input set from the full set
4. The leftover numbers are the missing one

e.g., 
full set: {1,2,3,4,5,6}
input set: {1,2,6}
Difference: {3,4,5} -> missing numbers
"""

def missing_number(nums, n):
    full_set = set(range(1, n + 1))
    num_set = set(nums)
    return sorted(full_set - num_set)

if __name__=="__main__":
    print(missing_number([1,2,6], 6))
    print(missing_number([1,2,3,5], 5))
    print(missing_number([], 3))
    print(missing_number([1,2,3,4], 4))