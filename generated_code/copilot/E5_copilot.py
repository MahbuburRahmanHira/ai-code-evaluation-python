import sys, ast, re

def _parse_prices(s)
    s = s.strip()
    if not s
        return []
    try
        val = ast.literal_eval(s)
        if isinstance(val, (list, tuple))
            res = []
            for x in val
                if isinstance(x, (int, float))
                    res.append(float(x))
                else
                    try
                        res.append(float(x))
                    except Exception
                        pass
            return res
        if isinstance(val, (int, float))
            return [float(val)]
    except Exception
        pass
    m = re.search(r'[[^]]+]', s)
    if m
        nums = re.findall(r'-d+(.d+)', m.group())
        return [float(x) for x in nums] if nums else []
    nums = re.findall(r'-d+(.d+)', s)
    return [float(x) for x in nums] if nums else []

def max_profit_one_transaction(prices)
    if not prices or len(prices)  2
        return 0.0
    min_price = float('inf')
    max_profit = 0.0
    for p in prices
        if p  min_price
            min_price = p
        else
            profit = p - min_price
            if profit  max_profit
                max_profit = profit
    return max_profit

def solve()
    data = sys.stdin.read()
    prices = _parse_prices(data)
    profit = max_profit_one_transaction(prices)
    if isinstance(profit, float) and profit.is_integer()
        print(int(profit))
    else
        print(profit)

if __name__ == __main__
    solve()