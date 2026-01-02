from typing import List
import heapq

def solve(nums: List[int], k: int) -> int:
    """
    Finds the kth largest element in an array using a min-heap of size k.
    
    The min-heap will store the k largest elements found so far.
    The root of the min-heap (the smallest element in the heap) will be the kth largest element.
    """
    if not nums or k <= 0 or k > len(nums):
        # Handle invalid inputs (e.g., empty list, k out of range)
        # Note: Depending on the problem specification, this might raise an error 
        # or return a specific default value. For this solution, 
        # we will assume valid inputs are provided based on typical competitive programming constraints.
        # If the problem strictly guarantees k is always valid, this check can be omitted.
        pass

    # 1. Initialize a min-heap with the first k elements
    # In Python, the `heapq` module implements a min-heap.
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    # 2. Iterate through the remaining elements (from index k to the end)
    for num in nums[k:]:
        # If the current number is larger than the smallest element in the heap (the root)
        if num > min_heap[0]:
            # Remove the smallest element (pop) and insert the new larger number (push)
            # This maintains a heap of size k containing the largest elements seen so far.
            heapq.heapreplace(min_heap, num)
            
    # 3. The root of the min-heap is the kth largest element
    # (it is the smallest among the k largest elements)
    return min_heap[0]

if __name__ == '__main__':
    # Test Case 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    # Sorted: [6, 5, 4, 3, 2, 1]. 2nd largest is 5.
    print(f"Input: {nums1}, k={k1}, Output: {solve(nums1, k1)}")

    # Test Case 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    # Sorted: [6, 5, 5, 4, 3, 3, 2, 2, 1]. 4th largest is 4.
    print(f"Input: {nums2}, k={k2}, Output: {solve(nums2, k2)}")
    
    # Test Case 3 (k=1, largest element)
    nums3 = [7, 6, 5, 4, 3, 2, 1]
    k3 = 1
    print(f"Input: {nums3}, k={k3}, Output: {solve(nums3, k3)}")

    # Test Case 4 (k=len(nums), smallest element)
    nums4 = [10, 5, 8]
    k4 = 3
    print(f"Input: {nums4}, k={k4}, Output: {solve(nums4, k4)}")