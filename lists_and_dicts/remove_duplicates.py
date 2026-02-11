"""
Problem:
Remove duplicates but keep original order.

Approach:
1. Set up - Create an empty set to track seen items and an empty list to store results.
2. Check each item - Loop through the original list one by one
    If item is not in seen set -> it's a new item
        Add it to seen set (so future duplicates are ignored)
        Append it to result list (maintains original order)
    If item is in seen set -> skip it (duplicate).
3. The result list contains only unique items in their original order.
"""

def remove_duplicates(nums):
    seen = set()
    result = []
    
    for i in nums:
        if i not in seen:
            seen.add(i)
            result.append(i)

    return result


if __name__=="__main__":
    nums = [1,2,2,3,4,4,5,6,7,8,9,0,0]
    print(f"Old result -> {nums} \nUnique items -> {remove_duplicates(nums)}")