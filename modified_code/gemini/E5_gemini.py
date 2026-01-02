def solve(prices: list[int] = None) -> int:
    if prices is None:
        prices = [7, 1, 5, 3, 6, 4]
    if not prices:
        return 0
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit
    return max_profit

if __name__ == '__main__':
    import timeit, cProfile

    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [1, 2],
        [],
        [5]
    ]

    def run_solver():
        for prices in test_cases:
            solve(prices)

    print("Profiling Best Time to Buy and Sell Stock solver:")
    cProfile.runctx('run_solver()', globals(), locals())
    t = timeit.timeit(run_solver, number=10000)
    print(f"Average execution time: {t/10000:.8f} sec")

    for prices in test_cases:
        result = solve(prices)
        print(f"Input: {prices} -> Maximum Profit: {result}")
