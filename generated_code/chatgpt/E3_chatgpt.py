def solve(n):
    if n < 0:
        return False
    s = str(n)
    return s == s[::-1]
