def solve(x: int = None) -> bool:
    if x is None:
        x = 121
    if x < 0:
        return False
    if x == 0:
        return True

    reverted_number = 0
    temp = x
    while temp > reverted_number:
        reverted_number = reverted_number * 10 + temp % 10
        temp //= 10

    return temp == reverted_number or temp == reverted_number // 10

if __name__ == '__main__':
    import timeit, cProfile

    test_cases = [121, -121, 10, 12321, 0, 1, 123]

    def run_solver():
        for x in test_cases:
            solve(x)

    print("Profiling Palindrome Number solver:")
    cProfile.runctx('run_solver()', globals(), locals())
    t = timeit.timeit(run_solver, number=10000)
    print(f"Average execution time: {t/10000:.8f} sec")

    for x in test_cases:
        result = solve(x)
        print(f"Input: {x} -> Output: {result}")
