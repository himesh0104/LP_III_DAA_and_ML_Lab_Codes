# -*- coding: utf-8 -*-
"""
DAA PRACTICAL 5: N-QUEENS PROBLEM WITH 1ST QUEEN FIXED (BACKTRACKING)
Savitribai Phule Pune University (SPPU) - LP-III

================================================================================
LAB TEST DEMO DATA TO TYPE IN TERMINAL:
================================================================================
CRITICAL VIVA POINT:
    The problem statement specifies placing Queen 1 at board[0][0], then placing
    the remaining queens using backtracking.
    - If N = 4: Placing queen at (0, 0) yields NO SOLUTION mathematically!
    - For N = 5 or N = 8: Valid solutions exist!

Recommended Demo Data to Type in Terminal:
    Enter value of N [Demo: 8]: 8
    (Or enter 5 for a smaller 5x5 board)

(Or simply press ENTER at the prompt to auto-load N = 8!)

Expected Solution Matrix for N = 8 (Queen 1 fixed at (0,0)):
    1 0 0 0 0 0 0 0
    0 0 0 0 0 0 1 0
    0 0 0 0 1 0 0 0
    0 0 0 0 0 0 0 1
    0 1 0 0 0 0 0 0
    0 0 0 1 0 0 0 0
    0 0 0 0 0 1 0 0
    0 0 1 0 0 0 0 0

Complexity Analysis:
    * Time Complexity:  O(N!) worst case
    * Space Complexity: O(N^2) for board + O(N) recursion stack
================================================================================
"""

def is_safe(board, row, col, n):
    """Checks whether placing a queen at board[row][col] is safe."""
    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    # Check left side of current row
    for k in range(col):
        if board[row][k] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    """Places queens column by column using backtracking."""
    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, col + 1, n):
                return True
            board[row][col] = 0  # Backtrack

    return False

def main():
    print("=" * 70)
    print(" DAA PRACTICAL 5: N-QUEENS (BACKTRACKING WITH 1ST QUEEN FIXED AT (0,0))")
    print("=" * 70)
    print("[LAB TEST DEMO DATA: Enter 8 (or 5)]")
    print("[NOTE: N=4 has no valid solution with Queen fixed at (0,0). Always use N=8 or 5]")
    print("-" * 70)

    raw_n = input("Enter value of N [Press Enter for demo: 8]: ").strip()
    n = int(raw_n) if raw_n else 8

    if n < 1:
        print("N must be a positive integer.")
        return

    board = [[0] * n for _ in range(n)]
    # Fix the first queen at row 0, col 0
    board[0][0] = 1

    print(f"\nSearching for solution on {n}x{n} board with Queen 1 fixed at (0, 0)...")
    success = solve_n_queens(board, 1, n)

    print("\n" + "=" * 70)
    if success:
        print(f"SUCCESS: {n}-QUEENS SOLUTION MATRIX FOUND:")
        print("-" * 70)
        for row in board:
            print("   " + " ".join(str(cell) for cell in row))
        print("-" * 70)
        print("Queen Coordinates (Row, Column) [0-indexed]:")
        for c in range(n):
            for r in range(n):
                if board[r][c] == 1:
                    print(f"  * Queen {c+1}: Row {r}, Column {c}")
    else:
        print(f"No solution exists for N = {n} with the first queen fixed at (0, 0).")
        if n == 4:
            print("  (Explanation: On a 4x4 board, queens can only be placed at columns")
            print("   [1,3,0,2] or [2,0,3,1]. No valid configuration allows a queen at (0,0)!)")

    print("=" * 70)
    print("COMPLEXITY ANALYSIS:")
    print("  * Time Complexity:  O(N!)")
    print("  * Space Complexity: O(N^2)")
    print("=" * 70)

if __name__ == "__main__":
    main()
