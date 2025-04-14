import random  # Import the random module

def n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == n:
            solutions.append(board[:])
            return

        cols = list(range(n))
        random.shuffle(cols)  # Shuffle columns for randomness
        for col in cols:
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    solutions = []
    solve([-1] * n, 0)
    return solutions

# Example: Solve the 4-Queens problem
n = 8
solutions = n_queens(n)
print(f"{n}-Queens Solutions:")
for solution in solutions:
    print(solution)
