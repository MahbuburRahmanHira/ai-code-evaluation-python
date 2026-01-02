# ----------------------------
# M1 ChatGPT: Longest substring without repeating characters
# ----------------------------
def longest_substring_no_repeat(s):
    if not s:
        return 0
    seen = {}
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# ----------------------------
# Step 5: Solver wrapper
# ----------------------------
def solve():
    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
        "abcdefg",
        "abba",
    ]
    results = []
    for s in test_cases:
        results.append(longest_substring_no_repeat(s))
    return results

# Optional profiling/timing if running directly
if __name__ == "__main__":
    import cProfile, timeit

    print("Profiling M1 ChatGPT solver...")
    cProfile.runctx('solve()', globals(), locals())

    t = timeit.timeit(solve, number=10000)
    print(f"\nAverage execution time over 10000 runs: {t/10000:.8f} sec")

    print("\nTest Outputs:")
    for idx, s in enumerate(["abcabcbb", "bbbbb", "pwwkew", "", "abcdefg", "abba"]):
        print(f"Input: '{s}', Output: {solve()[idx]}")
