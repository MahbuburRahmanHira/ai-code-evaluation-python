def longest_valid_parentheses(s=""):
    if not s:
        return 0

    max_len = 0
    stack = [-1]

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len

# Wrapper
def solve_wrapper():
    s = "(()())"
    return longest_valid_parentheses(s)

if __name__ == "__main__":
    print("H5 ChatGPT result:", solve_wrapper())  # Expected: 6
