def solve(s: str) -> bool:
    """
    Checks if a string containing parentheses/brackets is valid.
    
    A string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
    
    :param s: The input string containing brackets '()', '[]', '{}'.
    :return: True if the string is valid, False otherwise.
    """
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    
    for char in s:
        if char in mapping:
            # Closing bracket
            top_element = stack.pop() if stack else '#'
            
            # Check if stack is empty or the popped open bracket does not match the closing one
            if top_element != mapping[char]:
                return False
        else:
            # Opening bracket
            stack.append(char)
            
    # The string is valid if and only if the stack is empty at the end
    return not stack

if __name__ == '__main__':
    # Example 1
    # print(solve("()"))           # Expected: True
    
    # Example 2
    # print(solve("()[]{}"))       # Expected: True
    
    # Example 3
    # print(solve("(]"))           # Expected: False
    
    # Example 4
    # print(solve("([{}])"))       # Expected: True
    
    # Example 5
    # print(solve("{["))           # Expected: False
    
    # Example 6 (Edge case: Empty string)
    # print(solve(""))             # Expected: True
    
    # Example 7 (Edge case: Only closing bracket)
    # print(solve("]"))            # Expected: False