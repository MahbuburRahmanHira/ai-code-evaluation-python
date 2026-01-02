from typing import List
import timeit
import cProfile

def solve(nums1: List[int], nums2: List[int]) -> float:
    """
    Finds the median of two sorted arrays nums1 and nums2 in O(log(min(len(nums1), len(nums2)))) time.
    """
    m, n = len(nums1), len(nums2)
    if m > n:
        return solve(nums2, nums1)

    total_length = m + n
    half_len = (total_length + 1) // 2

    low, high = 0, m

    while low <= high:
        cut1 = low + (high - low) // 2
        cut2 = half_len - cut1

        L1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
        R1 = nums1[cut1] if cut1 < m else float('inf')
        L2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
        R2 = nums2[cut2] if cut2 < n else float('inf')

        if L1 <= R2 and L2 <= R1:
            if total_length % 2 == 1:
                return float(max(L1, L2))
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0
        elif L1 > R2:
            high = cut1 - 1
        else:
            low = cut1 + 1
    return 0.0

# ----------------------------
# Copilot-style wrapper
# ----------------------------
def solve_wrapper():
    test_cases = [
        ([1, 3], [2]),                 
        ([1, 2], [3, 4]),              
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]), 
        ([5, 6, 7], [1, 2, 3, 4]),     
    ]
    results = []
    for nums1, nums2 in test_cases:
        median = solve(nums1, nums2)
        results.append((nums1, nums2, median))
    return results

# ----------------------------
# Execution
# ----------------------------
if __name__ == '__main__':
    # Profiling
    def run_solver():
        for nums1, nums2, _ in solve_wrapper():
            solve(nums1, nums2)

    print("Profiling Median of Two Sorted Arrays solver:")
    cProfile.runctx('run_solver()', globals(), locals())

    # Timing
    t = timeit.timeit(run_solver, number=10000)
    print(f"Average execution time over 10000 runs: {t/10000:.8f} sec")

    # Print results
    for nums1, nums2, median in solve_wrapper():
        print(f"Input: {nums1}, {nums2} => Median: {median}")
