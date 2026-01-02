import ast
import re

# ----------------------------
# Original Copilot logic preserved
# ----------------------------
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

# ----------------------------
# Step 5: Wrapper for profiling
# ----------------------------
def solve(n=None):
    if n is None:
        n = 121  # default test input
    return is_palindrome_number(n)

if __name__ == "__main__":
    result = solve()
    print("E3_copilot is palindrome:", result)  # Expected: True
