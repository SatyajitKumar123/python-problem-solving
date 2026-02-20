"""
Problem:
Rotate [1,2,3,4,5] by k=2 -> [4,5,1,2,3]

Approach:
Using slicing:
- nums[-k:]  = Take last k elements (they become the new front)
- nums[:-k]  = Take all except last k (they become the new back)
- Add them together: last_k + rest = rotated list

For [1,2,3,4,5], k=2:
- Last 2: [4,5]
- Rest:   [1,2,3]
- Result: [4,5] + [1,2,3] = [4,5,1,2,3]
"""
def rotate_list(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]


if __name__ == "__main__":
    # Test cases
    print(rotate_list([1,2,3,4,5], 2))
    print(rotate_list([1,2,3,4,5], 7))
    print(rotate_list([1,2,3], 1))
    print(rotate_list([1,2,3], 4))
    print(rotate_list([1], 5))