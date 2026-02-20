"""
Problem:
Find the second largest element.

Approach:
1. Keep track of 1st place (largest) and 2nd place (second largest)
2. Start both as very small numbers (negative infinity)
3. Go through each number:
    - If current number beats 1st place -> old 1st becomes 2nd, current becomes 1st
    - If current number is between 1st and 2nd -> it becomes new 2nd
4. At the end, 2nd place is our answer
"""

def second_largest(nums):
    first = second = float('-inf')

    for n in nums:
        if n > first:
            second = first
            first = n
        elif first > n > second:
            second = n
    
    return second

if __name__=="__main__":
    print(second_largest([10, 5, 8, 20]))
    print(second_largest([10, 21, 22, 11, 15]))