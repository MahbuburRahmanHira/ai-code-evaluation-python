import re
import ast

# ----------------------------
def solve_n_queens(n=None):
    """
    Solve the N-Queens problem.
    n: integer, size of the chessboard
    Returns: list of solutions, each solution is a list of strings
    """
    if n is None or n <= 0:
        return []

    results = []
    queens = [-1] * n  # queens[row] = col

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
            cols.add(col)
            diag1.add(d1)
            diag2.add(d2)
            queens[row] = col
            backtrack(row + 1, cols, diag1, diag2)
            queens[row] = -1
            cols.remove(col)
            diag1.remove(d1)
            diag2.remove(d2)

    backtrack(0, set(), set(), set())
    return results

# ----------------------------
# Wrapper with built-in input
# ----------------------------
def solve_wrapper():
    n_val = 4  # Example test case
    return solve_n_queens(n_val)

# ----------------------------
if __name__ == "__main__":
    solutions = solve_wrapper()
    print("H4 Copilot N-Queens solutions for n=4:")
    for sol in solutions:
        for row in sol:
            print(row)
        print()  # empty line between solutions
