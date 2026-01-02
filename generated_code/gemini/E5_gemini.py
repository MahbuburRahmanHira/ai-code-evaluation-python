def solve(prices: list[int]) -> int:
    """
    Calculates the maximum profit from one transaction (one buy and one sell).

    :param prices: A list of stock prices where prices[i] is the price on day i.
    :return: The maximum profit, or 0 if no profit is possible.
    """
    if not prices:
        return 0
        
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            # Update the lowest price encountered so far
            min_price = price
        else:
            # Calculate the current profit if sold today and update max_profit
            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit
                
    return max_profit

if __name__ == '__main__':
    # Example 1
    # print(solve([7, 1, 5, 3, 6, 4])) # Expected: 5 (Buy at 1, Sell at 6)

    # Example 2
    # print(solve([7, 6, 4, 3, 1])) # Expected: 0 (No profit possible)

    # Example 3
    # print(solve([1, 2])) # Expected: 1 (Buy at 1, Sell at 2)

    # Example 4 (Edge case: empty list)
    # print(solve([])) # Expected: 0

    # Example 5 (Edge case: single element)
    # print(solve([5])) # Expected: 0