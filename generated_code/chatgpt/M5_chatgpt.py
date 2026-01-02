def solve(nums=None, k=1):
    if not nums or k < 1 or k > len(nums):
        return None
    nums_sorted = sorted(nums, reverse=True)
    return nums_sorted[k-1]
