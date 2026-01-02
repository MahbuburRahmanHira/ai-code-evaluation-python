import ast
import re

# ----------------------------
# Original Copilot logic preserved
# ----------------------------
def parse_list_literal(s):
    try:
        return list(ast.literal_eval(s))
    except Exception:
        return None

def two_sum_indices(nums, target):
    index_map = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in index_map:
            return index_map[needed], i
        index_map[num] = i
    return []

# ----------------------------
# Step 5: Uniform solve wrapper
# ----------------------------
def solve(s=None):
    if s is None:
        s = "[2,7,11,15]\n9"

    nums = None
    target = None

    try:
        val = ast.literal_eval(s)
        if isinstance(val, (list, tuple)):
            if len(val) == 2 and isinstance(val[0], (list, tuple)) and isinstance(val[1], (int, float)):
                nums = [int(x) for x in val[0]]
                target = int(val[1])
            elif all(isinstance(x, (int, float)) for x in val):
                if len(val) >= 2:
                    nums = [int(x) for x in val[:-1]]
                    target = int(val[-1])
    except Exception:
        pass

    if nums is None or target is None:
        lines = [ln.strip() for ln in s.splitlines() if ln.strip()]
        if len(lines) >= 2:
            lit = parse_list_literal(lines[0])
            nums = [int(x) for x in lit] if lit else [int(x) for x in re.findall(r'-?\d+', lines[0])]
            target = int(re.search(r'-?\d+', lines[1]).group())
        else:
            all_ints = [int(x) for x in re.findall(r'-?\d+', s)]
            if len(all_ints) >= 2:
                nums = all_ints[:-1]
                target = all_ints[-1]

    if nums is None or target is None:
        return None

    res = two_sum_indices(nums, target)
    if not res:
        return None
    return tuple(res)

if __name__ == "__main__":
    result = solve()
    print("E1_copilot two-sum indices:", result)
