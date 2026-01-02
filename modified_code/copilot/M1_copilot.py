import ast
import cProfile
import timeit

# ----------------------------
# Step 4: Original logic
# ----------------------------
def parse_input_string(data):
    """
    Parse input string from raw text.
    Returns the string to analyze.
    """
    s = data.strip()
    if not s:
        return ""
    try:
        v = ast.literal_eval(s)
        if isinstance(v, str):
            return v
        if isinstance(v, (list, tuple)) and len(v) > 0 and isinstance(v[0], str):
            return v[0]
    except Exception:
        pass
    lines = [ln for ln in s.splitlines() if ln.strip()]
    if lines:
        first = lines[0].strip()
        try:
            v = ast.literal_eval(first)
            if isinstance(v, str):
                return v
        except Exception:
            pass
        return first
    return s

def length_of_longest_substring(s):
    """
    Returns the length of the longest substring without repeating characters.
    """
    last_index = {}
    start = 0
    max_len = 0
    for i, ch in enumerate(s):
        if ch in last_index and last_index[ch] >= start:
            start = last_index[ch] + 1
        last_index[ch] = i
        max_len = max(max_len, i - start + 1)
    return max_len

# ----------------------------
# Step 5: Solver wrapper + test cases + profiling
# ----------------------------
def solve(input_str=None):
    test_inputs = [
        "abcabcbb",  # Expected: 3
        "bbbbb",     # Expected: 1
        "pwwkew",    # Expected: 3
        "",          # Expected: 0
        "au"         # Expected: 2
    ]
    results = []
    for s in test_inputs:
        results.append(length_of_longest_substring(s))
    return results

if __name__ == "__main__":
    # --- Profiling & Timing ---
    def run_solver():
        solve()

    print("Profiling M1 Copilot solver...")
    cProfile.runctx('run_solver()', globals(), locals())

    t = timeit.timeit(run_solver, number=10000)
    print(f"\nAverage execution time over 10000 runs: {t/10000:.8f} sec")

    # --- Output check ---
    outputs = solve()
    for i, s in enumerate(["abcabcbb", "bbbbb", "pwwkew", "", "au"]):
        print(f"Input: '{s}' => Longest unique substring length: {outputs[i]}")
