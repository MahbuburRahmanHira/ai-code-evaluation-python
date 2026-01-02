from typing import List

def solve(s: str) -> int:
    """
    Finds the length of the longest valid (well-formed) parentheses substring 
    using a stack-based approach.
    """
    n = len(s)
    if n < 2:
        return 0

    max_length = 0
    
    # Initialize the stack with -1. This serves as the baseline for the current 
    # valid substring's start index. If a valid substring ends at index i, 
    # its length is i - stack.top().
    stack: List[int] = [-1]

    for i in range(n):
        if s[i] == '(':
            # Push the index of '(' onto the stack
            stack.append(i)
        elif s[i] == ')':
            # Pop the top element, which should be the index of the matching '('
            stack.pop()

            if not stack:
                # If the stack is empty after popping, it means this ')' 
                # is the start of an invalid sequence (unmatched closing bracket).
                # Push the current index 'i' as the new baseline (the last index 
                # before the next potential valid substring).
                stack.append(i)
            else:
                # If the stack is not empty, a valid substring ends at index 'i'.
                # The length is calculated by i - stack.top(). 
                # stack.top() is the index of the unmatched character just before 
                # the current valid substring.
                current_length = i - stack[-1]
                max_length = max(max_length, current_length)
                
    return max_length

if __name__ == '__main__':
    # Test Case 1
    s1 = "(()"
    # Expected: 2 ("()")
    print(f"Input: '{s1}', Output: {solve(s1)}")

    # Test Case 2
    s2 = ")()())"
    # Expected: 4 ("()()")
    print(f"Input: '{s2}', Output: {solve(s2)}")

    # Test Case 3
    s3 = ""
    # Expected: 0
    print(f"Input: '{s3}', Output: {solve(s3)}")

    # Test Case 4
    s4 = "()(()"
    # Expected: 2 ("()")
    print(f"Input: '{s4}', Output: {solve(s4)}")
    
    # Test Case 5
    s5 = "()(())"
    # Expected: 6
    print(f"Input: '{s5}', Output: {solve(s5)}")