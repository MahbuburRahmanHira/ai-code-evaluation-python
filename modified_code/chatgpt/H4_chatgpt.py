def solve_n_queens(n=0):
    if n <= 0:
        return []

    solutions = []

    def backtrack(row, cols, diagonals, anti_diagonals, board):
        if row == n:
            solutions.append([''.join(r) for r in board])
            return
        for col in range(n):
            diag = row - col
            anti_diag = row + col
            if col in cols or diag in diagonals or anti_diag in anti_diagonals:
                continue
            cols.add(col)
            diagonals.add(diag)
            anti_diagonals.add(anti_diag)
            board[row][col] = 'Q'
            backtrack(row + 1, cols, diagonals, anti_diagonals, board)
            cols.remove(col)
            diagonals.remove(diag)
            anti_diagonals.remove(anti_diag)
            board[row][col] = '.'

    board = [['.'] * n for _ in range(n)]
    backtrack(0, set(), set(), set(), board)
    return solutions

# Wrapper
def solve_wrapper():
    n = 4
    return solve_n_queens(n)

if __name__ == "__main__":
    print("H4 ChatGPT result:", solve_wrapper())  # Expected: all 2 solutions for 4x4
