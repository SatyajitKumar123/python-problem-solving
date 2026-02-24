"""
Problem:
Given a list of integers and a target, return indices of two numbers such that they add up to the target

Example:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Approach:

"""

def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        diff = target - num
        
        if diff in seen:
            return [seen[diff], i]
        
        seen[num] = i

if __name__=="__main__":
    print(two_sum([2, 7, 11, 15], 9))    
    print(two_sum([3, 2, 4], 6))          
    print(two_sum([3, 3], 6))              
    print(two_sum([1, 2, 3, 4, 5], 8))   