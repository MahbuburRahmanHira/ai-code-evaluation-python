import ast
import re

# ----------------------------
# Original Copilot logic
# ----------------------------
def _parse_prices(s):
    s = s.strip()
    if not s:
        return []
    try:
        val = ast.literal_eval(s)
        if isinstance(val, (list, tuple)):
            return [float(x) for x in val]
        if isinstance(val, (int, float)):
            return [float(val)]
    except Exception:
        pass
    m = re.findall(r'-?\d+\.?\d*', s)
    return [float(x) for x in m] if m else []

def max_profit_one_transaction(prices):
    if not prices or len(prices) < 2:
        return 0.0
    min_price = float('inf')
    max_profit = 0.0
    for p in prices:
        if p < min_price:
            min_price = p
        else:
            profit = p - min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit

# ----------------------------
# Step 5 wrapper
# ----------------------------
def solve(prices_list=None):
    if prices_list is None:
        prices_list = [7,1,5,3,6,4]
    profit = max_profit_one_transaction(prices_list)
    return int(profit) if profit.is_integer() else profit

if __name__ == "__main__":
    result = solve()
    print("Maximum profit (Copilot):", result)  # Expected: 5
