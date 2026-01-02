def solve(s: str) -> int:
    """
    Given a string s, return the length of the longest substring without repeating characters.
    """
    n = len(s)
    if n == 0:
        return 0

    char_set = set()
    left = 0
    max_length = 0

    for right in range(n):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# ----------------------------
# Step 5: Wrapper for profiling & testing
# ----------------------------
def solve_wrapper():
    """
    No-argument wrapper to run multiple test cases for profiling/timing.
    """
    test_cases = ['abcabcbb', 'bbbbb', 'pwwkew', '', 'a', 'dvdf', ' ', 'au']
    results = []
    for s in test_cases:
        results.append(solve(s))
    return results

if __name__ == '__main__':
    import cProfile
    import timeit

    # --- Step 4 correctness tests ---
    test_cases = ['abcabcbb', 'bbbbb', 'pwwkew', '', 'a', 'dvdf', ' ', 'au']
    print("\n--- Step 4 Correctness Check ---")
    for s in test_cases:
        print(f"Input: '{s}', Output: {solve(s)}")

    # --- Step 5 Profiling & Timing ---
    print("\n--- Profiling & Timing M1 Gemini ---")
    cProfile.runctx('solve_wrapper()', globals(), locals())
    t = timeit.timeit(solve_wrapper, number=1000)
    print(f"\nAverage execution time over 1000 runs: {t/1000:.8f} sec")
