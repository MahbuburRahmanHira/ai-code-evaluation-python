# ----------------------------
# Original ChatGPT logic preserved
# ----------------------------
def solve(n):
    if n < 0:
        return False
    s = str(n)
    return s == s[::-1]

# ----------------------------
# Step 5: Wrapper for profiling
# ----------------------------
def solve_wrapper():
    test_input = 121
    return solve(test_input)

if __name__ == "__main__":
    result = solve_wrapper()
    print("E3_chatgpt is palindrome:", result)  # Expected: True
