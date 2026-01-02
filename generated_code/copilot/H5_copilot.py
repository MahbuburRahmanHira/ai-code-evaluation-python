import sys, ast

def _parse_input(data):
    s = data.strip()
    if not s:
        return ""
    try:
        v = ast.literal_eval(s)
        if isinstance(v, str):
            return v
    except Exception:
        pass
    lines = [l for l in s.splitlines() if l.strip()!='']
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

def longest_valid_parentheses(s):
    if not s:
        return 0
    stack = [-1]
    maxlen = 0
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            if not stack:
                stack.append(i)
            else:
                maxlen = max(maxlen, i - stack[-1])
        else:
            # treat other characters as break points
            stack = [i]
    return maxlen

def solve():
    data = sys.stdin.read()
    s = _parse_input(data)
    print(longest_valid_parentheses(s))

if __name__ == "__main__":
    solve()