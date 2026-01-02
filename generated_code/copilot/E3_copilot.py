import sys, ast, re

def is_palindrome_number(n):
    if n < 0:
        return False
    s = str(n)
    return s == s[::-1]

def parse_int(s):
    s = s.strip()
    if not s:
        return None
    try:
        v = ast.literal_eval(s)
        if isinstance(v, int):
            return v
        if isinstance(v, str) and re.fullmatch(r'-?\d+', v.strip()):
            return int(v.strip())
    except Exception:
        pass
    m = re.search(r'-?\d+', s)
    return int(m.group()) if m else None

def solve():
    data = sys.stdin.read()
    n = parse_int(data)
    res = False if n is None else is_palindrome_number(n)
    print(res)

if __name__ == "__main__":
    solve()