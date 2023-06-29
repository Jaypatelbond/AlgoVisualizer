N = 4
board = [[0] * N for _ in range(N)]


def is_attack(i, j):
    """
    Check if a queen placed at position (i, j) is under attack.

    Args:
        i (int): Row index.
        j (int): Column index.

    Returns:
        bool: True if the queen is under attack, False otherwise.
    """
    # Check if there is a queen in the same row or column
    for k in range(N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    # Check diagonals
    for k in range(N):
        for l in range(N):
            if k + l == i + j or k - l == i - j:
                if board[k][l] == 1:
                    return True

    return False


def N_queen(n):
    """
    Solve the N-Queens problem recursively.

    Args:
        n (int): Number of queens to be placed.

    Returns:
        bool: True if a valid arrangement of queens is found, False otherwise.
    """
    # Base case: all queens have been placed
    if n == 0:
        return True

    for i in range(N):
        for j in range(N):
            # Check if we can place a queen at position (i, j)
            if not is_attack(i, j) and board[i][j] != 1:
                board[i][j] = 1  # Place the queen

                # Recursion: check if we can place the next queen with this arrangement
                if N_queen(n - 1):
                    return True

                board[i][j] = 0  # Backtrack: remove the queen

    return False


def main():
    """
    Main function to solve the N-Queens problem for a given board size.
    """
    return N_queen(N)


if __name__ == "__main__":
    main()
