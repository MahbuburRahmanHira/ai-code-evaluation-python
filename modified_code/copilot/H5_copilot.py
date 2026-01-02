import ast

# ----------------------------
def longest_valid_parentheses(s):
    """
    Computes the length of the longest valid parentheses substring.
    s: input string
    returns: integer length
    """
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

# ----------------------------
def solve(input_str=None):
    """
    Wrapper function named 'solve' for benchmark compatibility.
    input_str: optional string argument; if None, uses built-in test input
    returns: integer length of longest valid parentheses
    """
    if input_str is None:
        # Built-in test string
        input_str = "(()())"
    s = input_str.strip()
    return longest_valid_parentheses(s)

# ----------------------------
if __name__ == "__main__":
    result = solve()
    print("H5 Copilot result for input '(()())':", result)  # Expected: 6
