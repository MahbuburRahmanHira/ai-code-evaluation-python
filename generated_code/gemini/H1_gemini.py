from typing import List

def solve(nums1: List[int], nums2: List[int]) -> float:
    """
    Finds the median of two sorted arrays nums1 and nums2 in O(log(min(len(nums1), len(nums2)))) time.
    This is achieved using the binary search method on the smaller array.
    """
    m = len(nums1)
    n = len(nums2)
    
    # Ensure nums1 is the shorter array for O(log(min(m, n))) complexity
    if m > n:
        return solve(nums2, nums1)

    total_length = m + n
    # The required number of elements in the left partition of the combined array
    half_len = (total_length + 1) // 2

    # Binary search range for the cut point in nums1
    low = 0
    high = m

    while low <= high:
        # Cut1 is the number of elements taken from nums1 into the left partition
        cut1 = low + (high - low) // 2
        
        # Cut2 is the number of elements taken from nums2 into the left partition
        cut2 = half_len - cut1

        # Determine the four elements needed for the median check:
        # L1: Leftmost element in the right partition of nums1 (or -infinity if cut1 = m)
        L1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
        # R1: Rightmost element in the left partition of nums1 (or +infinity if cut1 = m)
        R1 = nums1[cut1] if cut1 < m else float('inf')
        
        # L2: Leftmost element in the right partition of nums2 (or -infinity if cut2 = 0)
        L2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
        # R2: Rightmost element in the left partition of nums2 (or +infinity if cut2 = n)
        R2 = nums2[cut2] if cut2 < n else float('inf')

        if L1 <= R2 and L2 <= R1:
            # Partition is correct. Median is found.
            
            if total_length % 2 == 1:
                # Odd length: Median is the largest element in the left partition
                return float(max(L1, L2))
            else:
                # Even length: Median is the average of the two middle elements
                # which are the largest in the left partition and the smallest in the right partition.
                return (max(L1, L2) + min(R1, R2)) / 2.0
        elif L1 > R2:
            # Cut1 is too far to the right, need to move left in nums1
            high = cut1 - 1
        else: # L2 > R1 (which means R1 is too small)
            # Cut1 is too far to the left, need to move right in nums1
            low = cut1 + 1
            
    # This part should ideally not be reached if the input arrays are sorted.
    # It is a fallback for safety, though the problem constraints imply a median always exists.
    return 0.0

if __name__ == '__main__':
    # Test Case 1: Odd total length
    nums1_1 = [1, 3]
    nums2_1 = [2]
    # Combined: [1, 2, 3]. Median: 2.0
    print(f"Input: {nums1_1}, {nums2_1}, Output: {solve(nums1_1, nums2_1)}")

    # Test Case 2: Even total length
    nums1_2 = [1, 2]
    nums2_2 = [3, 4]
    # Combined: [1, 2, 3, 4]. Median: (2 + 3) / 2 = 2.5
    print(f"Input: {nums1_2}, {nums2_2}, Output: {solve(nums1_2, nums2_2)}")

    # Test Case 3: Empty array edge case (not strictly necessary since constraints usually ensure non-empty)
    # nums1_3 = [], nums2_3 = [1]. Combined: [1]. Median: 1.0
    # The initial swap handles this if one array is empty.
    nums1_3 = [1, 2, 3, 4, 5]
    nums2_3 = [6, 7, 8, 9, 10]
    # Combined: [1, ..., 10]. Median: (5 + 6) / 2 = 5.5
    print(f"Input: {nums1_3}, {nums2_3}, Output: {solve(nums1_3, nums2_3)}")
    
    # Test Case 4: Larger array first (testing the swap)
    nums1_4 = [5, 6, 7]
    nums2_4 = [1, 2, 3, 4]
    # Combined: [1, 2, 3, 4, 5, 6, 7]. Median: 4.0
    print(f"Input: {nums1_4}, {nums2_4}, Output: {solve(nums1_4, nums2_4)}")