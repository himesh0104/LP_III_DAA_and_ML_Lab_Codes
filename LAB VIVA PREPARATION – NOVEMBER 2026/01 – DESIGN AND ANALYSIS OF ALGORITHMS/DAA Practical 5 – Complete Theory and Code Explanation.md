# DAA Practical 5: N-Queens Problem with First Queen Placed (Backtracking)

## A. Practical Overview
- **Practical Number:** Group A - Practical 5 (Assignment No. 5)
- **Title:** N-Queens Matrix with First Queen Placed using Backtracking
- **Aim:** Design an $N$-Queens matrix having the first Queen placed. Use backtracking to place the remaining Queens to generate the final $N$-Queens matrix.
- **Objective:**
  1. Understand the state-space tree exploration in Backtracking.
  2. Implement constraint satisfaction and bounding functions (`is_safe`).
  3. Formulate the algorithm where Queen 1 is fixed at position `(0, 0)`.
  4. Analyze worst-case and average-case time complexities.
- **What Problem Does This Solve?**
  Place $N$ chess queens on an $N 	imes N$ chessboard such that no two queens attack each other. Two queens attack each other if they share the same row, column, or diagonal. The practical adds the specific constraint that the **first queen is pre-placed at `(0, 0)`**.
- **Why Is This Algorithm Required?**
  Brute force placement tests $inom{N^2}{N}$ configurations (for $N=8$, that is $pprox 4.4 	imes 10^9$ boards). Backtracking prunes invalid partial placements immediately, reducing the search space dramatically.
- **Real-World Applications:**
  - VLSI circuit layout design and chip wire routing (avoiding signal interference).
  - Resource scheduling, register allocation in compilers.
  - Constraint Satisfaction Problems (CSPs), such as Sudoku solvers and timetable generation.

---

## B. Theoretical Foundation
### 1. Chess Queen Attack Rules
A queen can move any number of squares horizontally, vertically, or diagonally.
Therefore:
1. No two queens can be in the same **row**.
2. No two queens can be in the same **column**.
3. No two queens can share the same **diagonal**:
   - Major diagonal (slope -1): difference `row - col` is constant.
   - Minor diagonal (slope +1): sum `row + col` is constant.

### 2. Backtracking Paradigm
Backtracking builds candidates incrementally and abandons ("backtracks") as soon as it determines the candidate cannot lead to a valid full solution:
- Place queens column by column (from col 1 to $N-1$).
- In column `col`, try placing the queen in `row` 0 to $N-1$.
- Check if `is_safe(board, row, col, n)` returns True.
- If safe, mark `board[row][col] = 1` and recurse for `col + 1`.
- If recursion returns False (dead end), reset `board[row][col] = 0` (backtrack!) and try the next row.

```
State Space Tree Pruning:
                       Root (Queen at 0,0)
                      /        |        \
               Col 1, Row 1  Col 1, Row 2  Col 1, Row 3
                 (Attack!)      (Safe)        (Safe)
                  [PRUNED]        |             |
                                Col 2...      Col 2...
```

### 3. Crucial University Viva Twist: First Queen Fixed at (0, 0)
- In standard $N$-Queens, for $N = 4$, there are **2 distinct solutions**:
  - Solution 1: Queens at `(1, 0), (3, 1), (0, 2), (2, 3)`
  - Solution 2: Queens at `(2, 0), (0, 1), (3, 2), (1, 3)`
- **NOTICE:** Neither of these valid solutions has a queen at row 0 of column 0!
- Therefore, if Queen 1 is fixed at `(0, 0)` for $N = 4$, **NO SOLUTION EXISTS!**
- The algorithm correctly backtracks and reports: `"No solution exists with the first queen fixed at (0, 0)."`.
- For $N \ge 8$ (e.g., standard $8 	imes 8$ board), valid solutions DO exist with Queen at `(0, 0)`.

---

## C. Complete Code Explanation

### Prescribed Practical Code:
```python
def is_safe(board, row, col, n):
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

    # Check left side of the row
    for j in range(col):
        if board[row][j] == 1:
            return False

    return True


def solve_n_queens(board, col, n):
    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens(board, col + 1, n):
                return True

            board[row][col] = 0

    return False


n = int(input("Enter value of N: "))

if n < 1:
    print("N must be positive.")
else:
    board = [[0] * n for _ in range(n)]

    # Fix the first queen at (0, 0)
    board[0][0] = 1

    if solve_n_queens(board, 1, n):
        print("N-Queens Matrix:")
        for row in board:
            print(*row)
    else:
        print("No solution exists with the first queen fixed at (0, 0).")
```

### Line-by-Line Breakdown:
1. `def is_safe(board, row, col, n):`
   - Bounding function that validates if placing a queen at `(row, col)` is attacked by any already placed queen.
   - **Why check only left side?** Because queens are placed column by column from left to right (columns $0 \dots col-1$). No queens exist to the right of `col`!
2. `while i >= 0 and j >= 0:`:
   - Moves diagonally up and left (`i -= 1, j -= 1`). Returns `False` if any `1` is encountered.
3. `while i < n and j >= 0:`:
   - Moves diagonally down and left (`i += 1, j -= 1`). Returns `False` if any `1` is encountered.
4. `for j in range(col):`:
   - Checks the entire horizontal row to the left (`board[row][j] == 1`).
5. `return True`:
   - If all three checks pass, the position is safe.
6. `def solve_n_queens(board, col, n):`:
   - Recursive backtracking search function.
7. `if col >= n: return True`:
   - **Base condition**: If `col` reaches $n$, all $n$ queens have been successfully placed without conflicts. Return `True`!
8. `for row in range(n):`:
   - Tries placing a queen in each row of the current column `col`.
9. `if is_safe(board, row, col, n):`:
   - Applies the bounding check.
10. `board[row][col] = 1`:
    - Chooses the placement: sets queen at `(row, col)`.
11. `if solve_n_queens(board, col + 1, n): return True`:
    - Recursively moves to the next column (`col + 1`). If the subproblem succeeds, propagate `True` upwards.
12. `board[row][col] = 0`:
    - **Backtracking Step:** If placing queen at `(row, col)` did not lead to a solution, reset the cell back to 0 so other rows can be tried.
13. `return False`:
    - If no row in column `col` is safe, returns `False` to force the previous column to backtrack.
14. `board[0][0] = 1`:
    - Fixes Queen 1 at coordinate `(0, 0)`.
15. `solve_n_queens(board, 1, n)`:
    - Initiates recursive backtracking starting at column 1 (since column 0 is already occupied).

---

## D. Algorithm / Pseudocode

```text
Algorithm SolveNQueens(Board, col, n):
1. If col >= n then:
     Return True
2. For row <- 0 to n - 1 do:
     If IsSafe(Board, row, col, n) is True then:
         Board[row][col] <- 1
         If SolveNQueens(Board, col + 1, n) == True then:
             Return True
         Board[row][col] <- 0  // Backtrack
3. Return False
```

### Complexities:
- **Time Complexity:**
  - Upper bound: $O(N!)$ because the first column has $N$ choices, second has at most $N-1$, third $N-2$, etc.
  - Practically, pruning eliminates the vast majority of branches, so actual run time is significantly lower.
- **Space Complexity:**
  - Board representation: $O(N^2)$ for the $N 	imes N$ matrix.
  - Recursion call stack: $O(N)$ depth (one frame per column).
  - **Overall Space Complexity:** $O(N^2)$ (or $O(N)$ if board is represented as a 1D array of column positions).

---

## E. High-Yield Viva Questions and Answers

**Q1: What paradigm does the N-Queens problem use?**
*Answer:* **Backtracking** (Depth-First Search with pruning via a bounding function).

**Q2: What is a Bounding Function?**
*Answer:* A function (`is_safe`) that tests whether a partial solution can potentially lead to a valid complete solution. If not, the algorithm immediately prunes that entire branch of the search tree.

**Q3: Why does `is_safe` only check the left side of the current column?**
*Answer:* Because queens are placed sequentially from left to right (column 0 to $N-1$). Columns to the right have not yet received any queens, so there is nothing to check there.

**Q4: For $N = 4$, what is the output when Queen 1 is fixed at (0, 0)?**
*Answer:* `"No solution exists with the first queen fixed at (0, 0)."`. The only valid 4-Queens solutions require Queen 1 to be at row 1 or row 2 of column 0.

**Q5: What is the smallest $N$ for which a solution exists with Queen 1 fixed at (0, 0)?**
*Answer:* $N = 1$ (trivial) and $N = 8$ (non-trivial). For $N = 4, 5, 6, 7$, placing at `(0, 0)` may fail or yield restricted configurations.

**Q6: What is the time complexity of the N-Queens algorithm?**
*Answer:* $O(N!)$ in the worst case.

**Q7: What is the auxiliary space complexity?**
*Answer:* $O(N)$ recursion stack depth and $O(N^2)$ for the chessboard matrix.

**Q8: What is the backtracking statement in the code?**
*Answer:* `board[row][col] = 0`. It resets the cell after an unsuccessful recursive exploration.

**Q9: What happens if you remove the line `board[row][col] = 0`?**
*Answer:* The algorithm will leave dead-end queens on the board, permanently blocking subsequent valid placements, leading to false negatives or incorrect board outputs.

**Q10: Can $N$-Queens be solved using a 1D array instead of a 2D matrix?**
*Answer:* Yes, an array `queen_pos[col] = row` of size $N$ can store the row index for each column, reducing space to $O(N)$.

**Q11: How can you check diagonal conflicts in $O(1)$ time?**
*Answer:* By maintaining three boolean lookup arrays for rows, major diagonals (`row - col + n - 1`), and minor diagonals (`row + col`).

**Q12: What is the difference between Backtracking and Branch & Bound?**
*Answer:*
- Backtracking uses **Depth-First Search (DFS)** and is suited for Constraint Satisfaction / Decision problems.
- Branch & Bound uses **Breadth-First Search (BFS) / Best-First Search** with a priority queue and is designed for Optimization problems.

**Q13: Does a solution exist for $N = 2$ and $N = 3$?**
*Answer:* No, $N = 2$ and $N = 3$ have no solutions under any circumstances.

**Q14: How many total solutions exist for standard 8-Queens?**
*Answer:* There are **92 total solutions** (12 unique fundamental solutions under rotation and reflection).

**Q15: What does `print(*row)` do in Python?**
*Answer:* It unpacks the elements of the list `row` and prints them separated by spaces on a single line.

**Q16: Why is `solve_n_queens(board, 1, n)` called with `1` instead of `0` in `main`?**
*Answer:* Because Queen 1 has already been fixed in column 0 at `board[0][0] = 1`, so searching must begin from column 1.

**Q17: Is N-Queens in P or NP?**
*Answer:* Finding all solutions is NP-Hard. Finding any single solution can be done in polynomial $O(N)$ time using explicit mathematical construction formulas.

**Q18: What is the condition `if col >= n: return True`?**
*Answer:* The base condition indicating that queens have been placed in all columns from 0 to $N-1$ without conflict.

**Q19: What type of graph traversal does backtracking emulate?**
*Answer:* Depth-First Search (DFS) on an implicit state-space tree.

**Q20: What is the role of `is_safe`?**
*Answer:* It acts as the **pruning criterion** or **bounding function** that cuts off non-viable branches of the state space tree early.

---

## F. Practical Examination Preparation
- **Must-Remember Lines:**
  - Backtrack reset: `board[row][col] = 0`
  - Base case: `if col >= n: return True`
  - Safe checks: Left row, Upper-left diagonal, Lower-left diagonal.
- **Examiner Trap:** "Run it for $N = 4$!"
  - *Be Ready:* When it outputs "No solution exists...", explain confidently: "Sir, this is mathematically correct! The only solutions for 4-queens require the first column queen at row 1 or row 2. Fixing it at (0, 0) leaves no valid configuration for the remaining columns."

---

## G. Quick Revision
1. **Technique:** Backtracking (DFS + Constraint Pruning).
2. **Fixed Condition:** `board[0][0] = 1`.
3. **Start Column:** `col = 1`.
4. **Pruning Function:** `is_safe(board, row, col, n)`.
5. **Checks in `is_safe`:** Left row, Upper-left diagonal, Lower-left diagonal.
6. **Time Complexity:** Worst case $O(N!)$.
7. **Space Complexity:** $O(N^2)$ board, $O(N)$ recursion depth.
8. **N = 4 Behavior:** No solution with Queen at (0, 0).
9. **Backtrack Action:** Unmark cell `board[row][col] = 0`.
10. **Top Viva Question:** "Why does backtracking check only the left side in `is_safe` and what happens when $N = 4$ with Queen 1 at (0, 0)?"
