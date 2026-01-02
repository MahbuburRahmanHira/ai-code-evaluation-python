import ast
import re
from collections import defaultdict
import cProfile
import timeit

# ----------------------------
# Step 4: Original logic
# ----------------------------
def _parse_words(s):
    """Parse a string into a list of words."""
    s = s.strip()
    if not s:
        return []
    try:
        val = ast.literal_eval(s)
        if isinstance(val, str):
            return val.split()
        if isinstance(val, (list, tuple)):
            return [str(x) for x in val]
    except Exception:
        pass
    # find quoted words
    quoted = re.findall(r"'([^']*)'|\"([^\"]*)\"", s)
    if quoted:
        res = []
        for a, b in quoted:
            res.append(a if a != "" else b)
        if res:
            return res
    # fallback: split on common separators and whitespace
    parts = re.split(r'[\s,;\[\]\(\)]+', s)
    parts = [p for p in parts if p]
    return parts

def group_anagrams(words):
    """Group a list of words into anagrams."""
    groups = defaultdict(list)
    for w in words:
        key = ''.join(sorted(w))
        groups[key].append(w)
    return list(groups.values())

# ----------------------------
# Step 5: Solver wrapper
# ----------------------------
def solve():
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        ["listen", "silent", "enlist", "google", "gogole"],
        [],
        ["a", "b", "c", "a"]
    ]
    results = []
    for words in test_cases:
        results.append(group_anagrams(words))
    return results

# ----------------------------
# Profiling & Timing
# ----------------------------
if __name__ == "__main__":
    print("Profiling M4 Copilot solver...")
    def run_solver():
        solve()
    cProfile.runctx('run_solver()', globals(), locals())

    t = timeit.timeit(run_solver, number=10000)
    print(f"\nAverage execution time over 10000 runs: {t/10000:.8f} sec")

    # Output check
    outputs = solve()
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        ["listen", "silent", "enlist", "google", "gogole"],
        [],
        ["a", "b", "c", "a"]
    ]
    for i, words in enumerate(test_cases):
        print(f"Input: {words} => Output: {outputs[i]}")
