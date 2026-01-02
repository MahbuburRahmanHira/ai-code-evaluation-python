from typing import List
import cProfile
import timeit

# ----------------------------
# Core solver (unchanged)
# ----------------------------
def solve(s: str) -> int:
    """
    Finds the length of the longest valid (well-formed) parentheses substring 
    using a stack-based approach.
    """
    n = len(s)
    if n < 2:
        return 0

    max_length = 0
    stack: List[int] = [-1]

    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                current_length = i - stack[-1]
                max_length = max(max_length, current_length)
                
    return max_length

# ----------------------------
# Step 5 wrapper for profiling / testing
# ----------------------------
def solve_wrapper():
    s = "()(())"  # standard test case
    return solve(s)

# ----------------------------
# Optional execution / profiling
# ----------------------------
if __name__ == '__main__':
    print("H4 Gemini result:", solve_wrapper())  # Expected: 6

    def run_solver():
        solve_wrapper()

    print("\nProfiling H4 Gemini solver:")
    cProfile.runctx('run_solver()', globals(), locals())

    t = timeit.timeit(run_solver, number=1000)
    print(f"Average execution time over 1000 runs: {t/1000:.8f} sec")
