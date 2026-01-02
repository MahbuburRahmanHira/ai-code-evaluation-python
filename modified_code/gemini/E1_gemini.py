# ----------------------------
# Original Gemini logic preserved
# ----------------------------
def solve(nums: list[int] = None, target: int = None) -> list[int]:
    if nums is None or target is None:
        nums, target = [2, 7, 11, 15], 9
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index
    return []

# ----------------------------
# Step 5: Profiling / Efficiency Measurement
# ----------------------------
if __name__ == '__main__':
    import timeit, cProfile

    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 2, 3], 7)
    ]

    def run_solver():
        for nums, target in test_cases:
            solve(nums, target)

    print("Profiling Two Sum solver:")
    cProfile.runctx('run_solver()', globals(), locals())
    t = timeit.timeit(run_solver, number=10000)
    print(f"Average execution time: {t/10000:.8f} sec")

    for nums, target in test_cases:
        result = solve(nums, target)
        print(f"Input: nums={nums}, target={target} -> Output: {result}")
