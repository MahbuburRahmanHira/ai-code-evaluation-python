import sys, ast, re, math

def _parse_list_literal(s):
    s = s.strip()
    if not s:
        return []
    try:
        v = ast.literal_eval(s)
        if isinstance(v, (list, tuple)):
            res = []
            for x in v:
                if isinstance(x, (int, float)):
                    res.append(float(x))
                elif isinstance(x, str):
                    x = x.strip()
                    if re.fullmatch(r'-?\d+(\.\d+)?', x):
                        res.append(float(x))
                else:
                    pass
            return res
    except Exception:
        pass
    nums = re.findall(r'-?\d+(?:\.\d+)?', s)
    return [float(x) for x in nums] if nums else []

def _extract_two_lists(s):
    s = s.strip()
    if not s:
        return [], []
    try:
        v = ast.literal_eval(s)
        if isinstance(v, (list, tuple)) and len(v) == 2:
            a, b = v[0], v[1]
            if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
                return _parse_list_literal(str(a)), _parse_list_literal(str(b))
    except Exception:
        pass
    lists = re.findall(r'\[[^\]]*\]', s)
    if len(lists) >= 2:
        a = _parse_list_literal(lists[0])
        b = _parse_list_literal(lists[1])
        return a, b
    lines = [ln.strip() for ln in s.splitlines() if ln.strip()]
    if len(lines) >= 2:
        a = _parse_list_literal(lines[0])
        b = _parse_list_literal(lines[1])
        return a, b
    m = re.search(r'^\s*\[.*\]\s*,\s*\[.*\]\s*$', s)
    if m:
        parts = s.split(',', 1)
        a = _parse_list_literal(parts[0])
        b = _parse_list_literal(parts[1])
        return a, b
    single = _parse_list_literal(s)
    if single:
        return single, []
    all_nums = re.findall(r'-?\d+(?:\.\d+)?', s)
    if all_nums:
        vals = [float(x) for x in all_nums]
        mid = len(vals) // 2
        return vals[:mid], vals[mid:]
    return [], []

def find_median_sorted_arrays(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        return None
    if m == 0:
        if n % 2 == 1:
            return B[n//2]
        else:
            return (B[n//2 - 1] + B[n//2]) / 2.0
    low, high = 0, m
    half_len = (m + n + 1) // 2
    while low <= high:
        i = (low + high) // 2
        j = half_len - i
        A_left = A[i-1] if i > 0 else -math.inf
        A_right = A[i] if i < m else math.inf
        B_left = B[j-1] if j > 0 else -math.inf
        B_right = B[j] if j < n else math.inf
        if A_left <= B_right and B_left <= A_right:
            if (m + n) % 2 == 1:
                return max(A_left, B_left)
            else:
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
        elif A_left > B_right:
            high = i - 1
        else:
            low = i + 1
    return None

def solve():
    data = sys.stdin.read()
    a, b = _extract_two_lists(data)
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    med = find_median_sorted_arrays(a_sorted, b_sorted)
    if med is None:
        print(None)
    else:
        if float(med).is_integer():
            print(int(med))
        else:
            print(med)

if __name__ == "__main__":
    solve()