# -*- coding: utf-8 -*-
"""
DAA PRACTICAL 3: FRACTIONAL KNAPSACK PROBLEM (GREEDY STRATEGY)
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
    Item 1: Ratio 6.00 -> Take 10.00 kg (Profit = 60.00)
    Item 2: Ratio 5.00 -> Take 20.00 kg (Profit = 100.00)
    Item 3: Ratio 4.00 -> Take 20/30 fraction = 0.667 (Profit = 80.00)
    Maximum Profit = 240.00

Complexity Analysis:
    * Time Complexity:  O(n log n) for sorting items by ratio
    * Space Complexity: O(1) auxiliary space beyond storage
================================================================================
"""

def fractional_knapsack(items, capacity):
    """
    Solves Fractional Knapsack using Greedy approach.
    items: list of (profit, weight, id)
    """
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_profit = 0.0
    breakdown = []
    remaining = capacity

    for profit, weight, item_id in items:
        if remaining == 0:
            break
        if weight <= remaining:
            total_profit += profit
            remaining -= weight
            breakdown.append((item_id, profit, weight, 1.0, profit))
        else:
            fraction = remaining / weight
            frac_profit = profit * fraction
            total_profit += frac_profit
            remaining = 0
            breakdown.append((item_id, profit, weight, fraction, frac_profit))

    return total_profit, breakdown

def main():
    print("=" * 70)
    print(" DAA PRACTICAL 3: FRACTIONAL KNAPSACK (GREEDY STRATEGY)")
    print("=" * 70)
    print("[LAB TEST DEMO DATA: 3 items -> (P:60, W:10), (P:100, W:20), (P:120, W:30), Cap: 50]")
    print("-" * 70)

    raw_n = input("Enter number of items [Press Enter for demo: 3]: ").strip()
    if not raw_n:
        print(">> Auto-loading Standard Demo Dataset (3 items, Capacity = 50)...")
        items = [(60.0, 10.0, "Item 1"), (100.0, 20.0, "Item 2"), (120.0, 30.0, "Item 3")]
        capacity = 50.0
    else:
        n = int(raw_n)
        items = []
        for i in range(n):
            p = float(input(f"  Enter profit for item {i+1}: ").strip())
            w = float(input(f"  Enter weight for item {i+1}: ").strip())
            items.append((p, w, f"Item {i+1}"))
        capacity = float(input("Enter knapsack capacity: ").strip())

    total_profit, breakdown = fractional_knapsack(items, capacity)

    print("\n" + "=" * 70)
    print("GREEDY SELECTION BREAKDOWN (SORTED BY PROFIT / WEIGHT):")
    print("-" * 70)
    print(f"{'Item':<10}{'Profit':<10}{'Weight':<10}{'Ratio':<12}{'Fraction':<15}{'Profit Added':<12}")
    print("-" * 70)
    for item_id, p, w, frac, earned in breakdown:
        print(f"{item_id:<10}{p:<10.2f}{w:<10.2f}{p/w:<12.2f}{frac:<15.3f}{earned:<12.2f}")

    print("-" * 70)
    print(f"Total Maximum Profit: {total_profit:.2f}")
    print("=" * 70)
    print("COMPLEXITY ANALYSIS:")
    print("  * Time Complexity:  O(n log n)")
    print("  * Space Complexity: O(1) auxiliary")
    print("=" * 70)

if __name__ == "__main__":
    main()
