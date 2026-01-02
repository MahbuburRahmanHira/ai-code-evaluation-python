def solve(nums: list[int], target: int) -> list[int]:
    """
    Finds the indices of two numbers in the list that add up to the target.

    :param nums: A list of integers.
    :param target: The target sum.
    :return: A list containing the two indices [index1, index2].
             Assumes exactly one solution exists.
    """
    num_map = {}  # Value -> Index
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index
    
    # According to the problem statement/typical Two Sum problem constraints, 
    # exactly one solution is guaranteed to exist, so this line might not be strictly 
    # necessary, but it handles the case where no solution is found.
    return []

if __name__ == '__main__':
    # Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solve(nums1, target1)
    # Expected: [0, 1] or [1, 0]
    # print(f"Input: nums={nums1}, target={target1}")
    # print(f"Output: {result1}")

    # Example 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solve(nums2, target2)
    # Expected: [1, 2] or [2, 1]
    # print(f"Input: nums={nums2}, target={target2}")
    # print(f"Output: {result2}")

    # Example 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solve(nums3, target3)
    # Expected: [0, 1] or [1, 0]
    # print(f"Input: nums={nums3}, target={target3}")
    # print(f"Output: {result3}")

    # Example 4 (No solution, though constraints usually guarantee one)
    nums4 = [1, 2, 3]
    target4 = 7
    result4 = solve(nums4, target4)
    # Expected: []
    # print(f"Input: nums={nums4}, target={target4}")
    # print(f"Output: {result4}")