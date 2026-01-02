import ast

# ----------------------------
# Original Copilot logic preserved
# ----------------------------
def _parse_input(s):
    s = s.strip()
    if not s:
        return ""
    try:
        val = ast.literal_eval(s)
        if isinstance(val, str):
            return val
    except Exception:
        pass
    lines = [l for l in s.splitlines() if l.strip() != '']
    if lines:
        return lines[0].strip()
    return s

def is_valid_parentheses(s):
    pairs = {')':'(', ']':'[', '}':'{'}
    openers = set(pairs.values())
    stack = []
    for ch in s:
        if ch in openers:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            continue
    return not stack

# ----------------------------
# Step 5: Wrapper for profiling
# ----------------------------
def solve(s=None):
    if s is None:
        s = "([]){}"
    parsed = _parse_input(s)
    return is_valid_parentheses(parsed)

if __name__ == "__main__":
    result = solve()
    print("E2_copilot valid parentheses:", result)  # Expected: True
