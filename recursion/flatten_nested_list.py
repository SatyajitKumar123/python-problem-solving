"""
Problem:
Flatten a nested list.

Approach:
1. Loot at each item in the list:
    - If it's NOT a box (not a list) -> put it in results
    - If it IS a box (a list) -> open it (call flatten again) and put everything inside in result
2. Keep doing this until all boxes are opened and all items are out
"""

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


if __name__=="__main__":
    
    print(flatten([1, [2, [3, 4]], 5]))
    print(flatten([1,[2,3,[4],[5,6]],7]))