# -*- coding: utf-8 -*-
"""
DAA PRACTICAL 4: 0-1 KNAPSACK PROBLEM (DYNAMIC PROGRAMMING)
Savitribai Phule Pune University (SPPU) - LP-III

================================================================================
LAB TEST DEMO DATA TO TYPE IN TERMINAL:
================================================================================
When prompted:
    Enter number of items [Demo: 3]: 3
    Enter profit for item 1: 60
    Enter weight for item 1: 10
    Enter profit for item 2: 100
    Enter weight for item 2: 20
    Enter profit for item 3: 120
    Enter weight for item 3: 30
    Enter knapsack capacity [Demo: 50]: 50

(Or simply press ENTER at the first prompt to auto-load all 3 items & capacity 50!)

Expected Output:
    Selected Items: Item 2 (Profit=100, Weight=20) and Item 3 (Profit=120, Weight=30)
    Total Weight = 50 <= Capacity 50
    Maximum Profit = 220

Key Difference to Explain in Viva:
    * Fractional Knapsack (Greedy): Items can be broken -> Max Profit = 240.0
    * 0-1 Knapsack (DP): Items CANNOT be broken (0 or 1) -> Max Profit = 220

Complexity Analysis:
    * Time Complexity:  O(n * W) pseudo-polynomial
    * Space Complexity: O(n * W) for 2D DP table
================================================================================
"""

def knapsack_01(profits, weights, capacity):
    """Solves 0-1 Knapsack using Dynamic Programming."""
    n = len(profits)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], profits[i - 1] + dp[i - 1][w - weights[i - 1]])

    # Backtrack to identify selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    selected.reverse()
    return dp[n][capacity], dp, selected

def main():
    print("=" * 70)
    print(" DAA PRACTICAL 4: 0-1 KNAPSACK (DYNAMIC PROGRAMMING)")
    print("=" * 70)
    print("[LAB TEST DEMO DATA: 3 items -> (P:60, W:10), (P:100, W:20), (P:120, W:30), Cap: 50]")
    print("-" * 70)

    raw_n = input("Enter number of items [Press Enter for demo: 3]: ").strip()
    if not raw_n:
        print(">> Auto-loading Standard Demo Dataset (3 items, Capacity = 50)...")
        profits = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
    else:
        n = int(raw_n)
        profits = []
        weights = []
        for i in range(n):
            p = int(input(f"  Enter profit for item {i+1}: ").strip())
            w = int(input(f"  Enter weight for item {i+1}: ").strip())
            profits.append(p)
            weights.append(w)
        capacity = int(input("Enter knapsack capacity: ").strip())

    max_profit, dp_table, selected_indices = knapsack_01(profits, weights, capacity)

    print("\n" + "=" * 70)
    print(f"MAXIMUM PROFIT ACHIEVED: {max_profit}")
    print("-" * 70)
    print("ITEMS SELECTED IN OPTIMAL KNAPSACK:")
    tot_w = 0
    for idx in selected_indices:
        print(f"  * Item {idx+1}: Profit = {profits[idx]}, Weight = {weights[idx]}")
        tot_w += weights[idx]
    print(f"Total Weight Used: {tot_w} / {capacity}")

    print("\nDP TABLE PREVIEW (Last 5 columns):")
    header = "Item \\ W " + "".join(f"{w:>7}" for w in range(max(0, capacity - 4), capacity + 1))
    print(header)
    for i in range(len(profits) + 1):
        row_str = f"{i:>8} " + "".join(f"{dp_table[i][w]:>7}" for w in range(max(0, capacity - 4), capacity + 1))
        print(row_str)

    print("=" * 70)
    print("COMPLEXITY ANALYSIS:")
    print("  * Time Complexity:  O(n * W)")
    print("  * Space Complexity: O(n * W)")
    print("=" * 70)

if __name__ == "__main__":
    main()
