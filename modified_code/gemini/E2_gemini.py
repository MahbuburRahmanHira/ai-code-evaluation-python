def solve(s: str = None) -> bool:
    if s is None:
        s = "()[]{}"
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if top_element != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack

if __name__ == '__main__':
    import timeit, cProfile

    test_cases = ["()", "()[]{}", "(]", "([{}])", "{[", "", "]"]

    def run_solver():
        for s in test_cases:
            solve(s)

    print("Profiling Valid Parentheses solver:")
    cProfile.runctx('run_solver()', globals(), locals())
    t = timeit.timeit(run_solver, number=10000)
    print(f"Average execution time: {t/10000:.8f} sec")

    for s in test_cases:
        result = solve(s)
        print(f"Input: {s} -> Output: {result}")
