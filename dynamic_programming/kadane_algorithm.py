"""
Problem:
Find the maximum sum of any contiguous subarray.

Approach:
Imagine you're walking through numbers and keeping a running total.

At each number, you have two choices:
1. Start fresh with just this number (forget the past)
2. Add this number to your previous total (continue the streak)

Pick whichever gives you a better total RIGHT NOW.

Then ask yourself: "Is this the best total I've ever seen?"
If yes, remember it.
"""

def max_subarray(nums):
    if not nums:
        return 0
    
    current = maximum = nums[0]

    for n in nums[1:]:
        current = max(n, current + n)

        maximum = max(maximum, current)
    
    return maximum

if __name__=="__main__":
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],  
        [1],                                
        [-1, -2, -3],                       
        [5, 4, -1, 7, 8],                    
        [-2, -1],                            
        [],                                 
    ]
    
    for nums in test_cases:
        result = max_subarray(nums)
        print(f"Array: {nums}")
        print(f"Max subarray sum: {result}")

        