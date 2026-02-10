"""
Problem:
Return duplicate elements from a list.

Aproach:
We use two sets to track numbers:
1. 'seen' set: Stores all numbers we've encountered
2. 'duplicates' set: Stores numbers that appear more than once

For each number in the list:
- If it's NOT in 'seen', add it to 'seen'
- If it's already in 'seen', add it to 'duplicates'

Finally, convert the duplicates set to a list and return it.
"""

def find_duplicates(nums):
    seen = set()
    duplicates = set()
    
    for i in nums:
        if i not in seen:
            seen.add(i)
        else:
            duplicates.add(i)
    return list(duplicates)


if __name__ == "__main__":
    list1 = [1,2,2,3,4,4,5,6,6,7,8,9,0,0]
    print(f"duplicates in {list1} are {find_duplicates(list1)}")