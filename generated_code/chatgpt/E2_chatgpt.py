def solve(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            continue
    
    return not stack
