# -*- coding: utf-8 -*-
"""
ALL DAA PRACTICAL PROGRAMS (1 TO 5)
Savitribai Phule Pune University (SPPU) - LP-III
Authored for Viva & Practical Exam Mastery
"""

import heapq

# =============================================================
# DAA PRACTICAL 1: FIBONACCI NUMBERS (RECURSIVE & NON-RECURSIVE)
# =============================================================
def fib_recursive(n):
    """Recursive Fibonacci - O(2^n) time, O(n) space"""
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def run_daa1():
    print("\n--- DAA PRACTICAL 1: FIBONACCI NUMBERS ---")
    n = int(input("Enter number of terms (e.g., 10): "))

    print("Non-recursive Fibonacci:")
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print("\nRecursive Fibonacci:")
    for i in range(n):
        print(fib_recursive(i), end=" ")
    print()

# =============================================================
# DAA PRACTICAL 2: HUFFMAN ENCODING (GREEDY STRATEGY)
# =============================================================
def huffman(characters, frequencies):
    """Huffman Encoding using Min-Heap - O(n log n) time, O(n) space"""
    heap = []
    for i in range(len(characters)):
        heapq.heappush(heap, (frequencies[i], i, characters[i]))

    counter = len(characters)

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        node = (left, right)
        heapq.heappush(heap, (f1 + f2, counter, node))
        counter += 1

    def print_codes(node, code=""):
        if isinstance(node, str):
            print(f"  {node} : {code if code else '0'}")
            return
        left, right = node
        print_codes(left, code + "0")
        print_codes(right, code + "1")

    if heap:
        print("\nHuffman Codes:")
        print_codes(heap[0][2])

def run_daa2():
    print("\n--- DAA PRACTICAL 2: HUFFMAN ENCODING ---")
    n = int(input("Enter number of characters (e.g., 4): "))
    characters, frequencies = [], []
    for i in range(n):
        ch = input(f"Enter character {i+1}: ")
        freq = int(input(f"Enter frequency for '{ch}': "))
        characters.append(ch)
        frequencies.append(freq)
    huffman(characters, frequencies)

# =============================================================
# DAA PRACTICAL 3: FRACTIONAL KNAPSACK (GREEDY METHOD)
# =============================================================
def fractional_knapsack(items, capacity):
    """Fractional Knapsack - O(n log n) time, O(1) space"""
    # Sort descending by ratio profit / weight
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_profit = 0.0

    for profit, weight in items:
        if capacity == 0:
            break
        if weight <= capacity:
            total_profit += profit
            capacity -= weight
        else:
            total_profit += profit * (capacity / weight)
            capacity = 0

    return total_profit

def run_daa3():
    print("\n--- DAA PRACTICAL 3: FRACTIONAL KNAPSACK ---")
    n = int(input("Enter number of items (e.g., 3): "))
    items = []
    for i in range(n):
        profit = float(input(f"Enter profit of item {i+1}: "))
        weight = float(input(f"Enter weight of item {i+1}: "))
        items.append((profit, weight))
    capacity = float(input("Enter knapsack capacity: "))
    max_prof = fractional_knapsack(items, capacity)
    print(f"Maximum Profit: {max_prof}")

# =============================================================
# DAA PRACTICAL 4: 0-1 KNAPSACK (DYNAMIC PROGRAMMING)
# =============================================================
def knapsack_01(profits, weights, capacity):
    """0-1 Knapsack using 2D DP - O(n * W) pseudo-polynomial time"""
    n = len(profits)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
    return dp[n][capacity]

def run_daa4():
    print("\n--- DAA PRACTICAL 4: 0-1 KNAPSACK ---")
    n = int(input("Enter number of items (e.g., 2): "))
    profits, weights = [], []
    for i in range(n):
        profits.append(int(input(f"Enter profit of item {i+1}: ")))
        weights.append(int(input(f"Enter weight of item {i+1}: ")))
    capacity = int(input("Enter knapsack capacity: "))
    max_prof = knapsack_01(profits, weights, capacity)
    print(f"Maximum Profit: {max_prof}")

# =============================================================
# DAA PRACTICAL 5: N-QUEENS (BACKTRACKING WITH 1ST QUEEN FIXED)
# =============================================================
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
            board[row][col] = 0  # Backtrack!

    return False

def run_daa5():
    print("\n--- DAA PRACTICAL 5: N-QUEENS (1ST QUEEN FIXED AT (0,0)) ---")
    n = int(input("Enter value of N (e.g., 4 or 8): "))
    if n < 1:
        print("N must be positive.")
        return

    board = [[0] * n for _ in range(n)]
    # Fix the first queen at (0, 0)
    board[0][0] = 1

    if solve_n_queens(board, 1, n):
        print("\nN-Queens Matrix Solution:")
        for row in board:
            print(" ".join(str(cell) for cell in row))
    else:
        print("No solution exists with the first queen fixed at (0, 0).")

# =============================================================
# INTERACTIVE EXECUTION MENU
# =============================================================
if __name__ == "__main__":
    while True:
        print("\n==========================================")
        print("   DAA PRACTICAL CODE EXECUTION MENU     ")
        print("==========================================")
        print("1. Practical 1: Fibonacci Numbers (Recursive & Iterative)")
        print("2. Practical 2: Huffman Encoding (Greedy Strategy)")
        print("3. Practical 3: Fractional Knapsack (Greedy Strategy)")
        print("4. Practical 4: 0-1 Knapsack (Dynamic Programming)")
        print("5. Practical 5: N-Queens (Backtracking)")
        print("0. Exit")
        choice = input("Select an option (0-5): ").strip()
        if choice == "1": run_daa1()
        elif choice == "2": run_daa2()
        elif choice == "3": run_daa3()
        elif choice == "4": run_daa4()
        elif choice == "5": run_daa5()
        elif choice == "0": break
        else: print("Invalid selection.")
