"""
Problem:
Find all pairs in a list that sum to a target.

Approach:
Think of it like finding dance partners at a party:

1. Keep a "seen" set to remember numbers you've already encountered
2. For each new number:
   - Calculate its needed partner: target - current number
   - If that partner is in "seen" → found a pair! Record it
   - If not → add current number to "seen" for future matches
3. Continue until you've checked all numbers

This works in one pass because any pair will be discovered when we encounter the second number.
"""

def find_pairs(nums, target):
    seen = set()
    pairs = []
    
    for num in nums:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
        
    return pairs


if __name__=="__main__":
    print(find_pairs([1,2,3,4,5], 5))
    print(find_pairs([1,2,3,4,5], 6))
    print(find_pairs([1,1,2,3], 4))
    print(find_pairs([], 5))