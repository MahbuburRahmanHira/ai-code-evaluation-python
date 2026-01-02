import sys, ast, re

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
    # try whole literal like ([1,2,3], 2) or ([1,2,3],2)
    try:
        val = ast.literal_eval(s)
        if isinstance(val, (list, tuple)) and len(val) == 2 and isinstance(val[0], (list, tuple)) and isinstance(val[1], (int, float)):
            nums = [int(x) if isinstance(x, int) else (int(x) if isinstance(x, float) and x.is_integer() else x) for x in list(val[0])]
            k = int(val[1])
            return nums, k
    except Exception:
        pass
    # split lines
    lines = [ln.strip() for ln in s.splitlines() if ln.strip()]
    if len(lines) >= 2:
        # first line nums, second line k
        lit = _parse_list_literal(lines[0])
        if lit is not None:
            nums = [int(x) if isinstance(x, (int, float)) and float(x).is_integer() else x for x in lit]
        else:
            nums = [int(x) for x in re.findall(r'-?\d+', lines[0])]
        k = _extract_int(lines[1])
        return nums, k
    # single-line cases
    # find a list literal
    m = re.search(r'\[[^\]]*\]', s)
    if m:
        lit = _parse_list_literal(m.group())
        if lit is not None:
            nums = [int(x) if isinstance(x, (int, float)) and float(x).is_integer() else x for x in lit]
            after = s[m.end():]
            k = _extract_int(after)
            if k is not None:
                return nums, k
            # maybe integer before the list
            before = s[:m.start()]
            k = _extract_int(before)
            return nums, k
    # fallback: all ints in string, last is k, rest are nums
    all_ints = [int(x) for x in re.findall(r'-?\d+', s)]
    if len(all_ints) >= 2:
        return all_ints[:-1], all_ints[-1]
    # if only a list literal without k
    lit = _parse_list_literal(s)
    if lit is not None:
        nums = [int(x) if isinstance(x, (int, float)) and float(x).is_integer() else x for x in lit]
        return nums, None
    return [], None

def kth_largest(nums, k):
    if not nums or k is None:
        return None
    n = len(nums)
    if k <= 0 or k > n:
        return None
    try:
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[k-1]
    except Exception:
        return None

def solve():
    data = sys.stdin.read()
    nums, k = parse_input(data)
    res = kth_largest(nums, k)
    if res is None:
        print(None)
    else:
        if isinstance(res, float) and res.is_integer():
            print(int(res))
        else:
            print(res)

if __name__ == "__main__":
    solve()