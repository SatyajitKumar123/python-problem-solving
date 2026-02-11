"""
Problem:
Merge two sorted lists into one sorted list.

Approach:
1. Set up - Create two pointers (i and j) at the start of both lists and an empty result list
2. Compare and pick - Look at current numbers in both lists, take the smaller one, add it to result, move that lists pointer forward
3. Repeat - Keep comparing until one list runs out of numbers
4. Add leftovers - Whatever numbers remain in the other list get added to the end (they're already sorted)
"""

def merge_lists(a, b):
    i = j = 0
    result = []
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    
    result.extend(a[i:])
    result.extend(b[j:])
    return result

if __name__=="__main__":
    a = [2,4,6]
    b = [1,3,5,7]
    print(merge_lists(a, b))
