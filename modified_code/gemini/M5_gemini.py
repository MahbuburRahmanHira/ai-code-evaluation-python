import heapq

def kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for n in nums[k:]:
        if n > heap[0]:
            heapq.heapreplace(heap, n)
    return heap[0]

# --- Wrapper solve() for benchmark ---
def solve():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    return kth_largest(nums, k)
