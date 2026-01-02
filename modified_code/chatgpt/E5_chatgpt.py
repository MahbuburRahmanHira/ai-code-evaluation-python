# ----------------------------
# Original ChatGPT logic
# ----------------------------
def solve(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit

# ----------------------------
# Step 5 wrapper
# ----------------------------
def solve_wrapper():
    example_prices = [7, 1, 5, 3, 6, 4]
    return solve(example_prices)

if __name__ == "__main__":
    result = solve_wrapper()
    print("Maximum profit (ChatGPT):", result)  # Expected: 5
