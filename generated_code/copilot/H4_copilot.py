import sys, ast, re

def solve():
    data = sys.stdin.read()
    if not data:
        print([]); return
    s = data.strip()
    n = None
    try:
        val = ast.literal_eval(s)
        if isinstance(val, int):
            n = val
    except Exception:
        pass
    if n is None:
        m = re.search(r'-?\d+', s)
        if m:
            try:
                n = int(m.group())
            except Exception:
                n = None
    if n is None or n <= 0:
        print([]); return

    results = []
    queens = [-1] * n

    def backtrack(row, cols, diag1, diag2):
        if row == n:
            board = []
            for r in range(n):
                row_chars = ['.'] * n
                row_chars[queens[r]] = 'Q'
                board.append(''.join(row_chars))
            results.append(board)
            return
        for col in range(n):
            d1 = row - col
            d2 = row + col
            if col in cols or d1 in diag1 or d2 in diag2:
                continue
            cols.add(col); diag1.add(d1); diag2.add(d2)
            queens[row] = col
            backtrack(row + 1, cols, diag1, diag2)
            queens[row] = -1
            cols.remove(col); diag1.remove(d1); diag2.remove(d2)

    backtrack(0, set(), set(), set())
    print(results)

if __name__ == "__main__":
    solve()