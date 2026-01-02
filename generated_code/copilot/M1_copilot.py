import sys, ast

def _parse_input(data):
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
    last_index = {}
    start = 0
    max_len = 0
    for i, ch in enumerate(s):
        if ch in last_index and last_index[ch] >= start:
            start = last_index[ch] + 1
        last_index[ch] = i
        cur_len = i - start + 1
        if cur_len > max_len:
            max_len = cur_len
    return max_len

def solve():
    data = sys.stdin.read()
    s = _parse_input(data)
    print(length_of_longest_substring(s))

if __name__ == "__main__":
    solve()