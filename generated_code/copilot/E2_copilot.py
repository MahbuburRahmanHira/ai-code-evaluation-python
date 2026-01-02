import sys, ast

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
    lines = [l for l in s.splitlines() if l.strip()!='']
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

def solve():
    data = sys.stdin.read()
    s = _parse_input(data)
    print(is_valid_parentheses(s))

if __name__ == "__main__":
    solve()