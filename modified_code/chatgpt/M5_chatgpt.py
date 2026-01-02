def kth_largest(nums, k):
    if not nums or k < 1 or k > len(nums):
        return None
    return sorted(nums, reverse=True)[k-1]

def solve():
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2),
        ([7, 10, 4, 3, 20, 15], 3),
        ([1, 2], 1)
    ]
    results = []
    for nums, k in test_cases:
        results.append(kth_largest(nums, k))
    return results
