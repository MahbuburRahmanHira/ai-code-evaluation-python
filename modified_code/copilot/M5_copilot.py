import sys, ast, re
from typing import Optional

def _parse_list_literal(s):
    try:
        v = ast.literal_eval(s)
        if isinstance(v, (list, tuple)):
            return list(v)
    except Exception:
        pass
    return None

def _extract_int(s):
    m = re.search(r'-?\d+', s)
    if m:
        return int(m.group())
    return None

def parse_input(data):
    s = data.strip()
    if not s:
        return [], None
    try:
        val = ast.literal_eval(s)
        if isinstance(val, (list, tuple)) and len(val) == 2 and isinstance(val[0], (list, tuple)) and isinstance(val[1], (int, float)):
            nums = [int(x) for x in val[0]]
            k = int(val[1])
            return nums, k
    except Exception:
        pass
    lines = [ln.strip() for ln in s.splitlines() if ln.strip()]
    if len(lines) >= 2:
        lit = _parse_list_literal(lines[0])
        nums = [int(x) for x in lit] if lit else [int(x) for x in re.findall(r'-?\d+', lines[0])]
        k = _extract_int(lines[1])
        return nums, k
    m = re.search(r'\[[^\]]*\]', s)
    if m:
        lit = _parse_list_literal(m.group())
        if lit:
            nums = [int(x) for x in lit]
            after = s[m.end():]
            k = _extract_int(after) or _extract_int(s[:m.start()])
            return nums, k
    all_ints = [int(x) for x in re.findall(r'-?\d+', s)]
    if len(all_ints) >= 2:
        return all_ints[:-1], all_ints[-1]
    lit = _parse_list_literal(s)
    if lit:
        return [int(x) for x in lit], None
    return [], None

def kth_largest(nums, k):
    if not nums or k is None or k < 1 or k > len(nums):
        return None
    return sorted(nums, reverse=True)[k-1]

# Step 5 solver wrapper
def solve_kth_largest(input_str: Optional[str] = None):
    if input_str is None:
        input_str = sys.stdin.read()
    nums, k = parse_input(input_str)
    return kth_largest(nums, k)

# ----------------------------
# Wrapper function for benchmark
def solve():
    test_cases = [
        "[3,2,1,5,6,4], 2",
        "[3,2,3,1,2,4,5,5,6], 4",
        "1 2 3 4 5\n3",
        "[10,20,30]",
        "[], 1",
    ]
    results = [solve_kth_largest(tc) for tc in test_cases]
    return results

# Optional profiling and local test
if __name__ == "__main__":
    import cProfile, timeit

    print("--- Profiling M5 Copilot ---")
    def run_solver():
        solve()
    cProfile.runctx('run_solver()', globals(), locals())
    t = timeit.timeit(run_solver, number=10000)
    print(f"\nAverage execution time over 10000 runs: {t/10000:.8f} sec")

    print("\n--- Test Outputs ---")
    for tc in [
        "[3,2,1,5,6,4], 2",
        "[3,2,3,1,2,4,5,5,6], 4",
        "1 2 3 4 5\n3",
        "[10,20,30]",
        "[], 1",
    ]:
        print(f"Input: {tc} => Output: {solve_kth_largest(tc)}")
