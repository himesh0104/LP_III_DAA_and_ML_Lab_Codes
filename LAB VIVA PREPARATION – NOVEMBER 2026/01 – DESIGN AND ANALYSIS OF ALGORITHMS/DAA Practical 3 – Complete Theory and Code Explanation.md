+# DAA Practical 3: Fractional Knapsack Problem (Greedy Method)

## A. Practical Overview
- **Practical Number:** Group A - Practical 3 (Assignment No. 3)
- **Title:** Fractional Knapsack Problem using Greedy Strategy
- **Aim:** Write a program to solve the Fractional Knapsack problem using a greedy method and analyze its time and space complexity.
- **Objective:**
  1. Understand the formulation of the Knapsack optimization problem.
  2. Implement the greedy strategy based on value-to-weight ratio ($rac{P_i}{W_i}$).
  3. Understand how item divisibility allows a greedy choice to yield an optimal solution.
  4. Compare the fractional knapsack with the 0/1 knapsack problem.
- **What Problem Does This Solve?**
  Given a set of $n$ items, each with a profit $p_i$ and weight $w_i$, and a knapsack of maximum capacity $W$, fill the knapsack to maximize total profit. In the **fractional** version, items are divisible (like grains, liquids, or powders); any fraction $x_i \in [0, 1]$ of an item may be selected.
- **Why Is This Algorithm Required?**
  It provides an optimal solution in $O(n \log n)$ time, whereas non-divisible knapsack variants are NP-Complete.
- **Real-World Applications:**
  - Resource allocation where resources are continuous (bandwidth allocation, CPU time sharing).
  - Cargo loading with divisible commodities (crude oil, chemical powders, food grains).
  - Portfolio investment budgeting with fractional shares.

---

## B. Theoretical Foundation
### 1. Mathematical Formulation
Maximize:
$$\sum_{i=1}^n p_i \cdot x_i$$
Subject to:
$$\sum_{i=1}^n w_i \cdot x_i \le W \quad 	ext{and} \quad 0 \le x_i \le 1 \quad orall i \in \{1, \dots, n\}$$

### 2. The Greedy Choice: Value Density ($rac{p_i}{w_i}$)
To maximize profit per unit weight consumed, we compute the profit-to-weight ratio $r_i = rac{p_i}{w_i}$ for every item and sort them in descending order:
$$r_1 \ge r_2 \ge \dots \ge r_n$$
We greedily select items with the highest ratio:
- If remaining knapsack capacity $\ge w_i$, take the whole item ($x_i = 1$).
- If remaining capacity $< w_i$, take a fraction $x_i = rac{	ext{capacity}}{w_i}$, fill the bag to 100%, and stop.

### 3. Why Greedy Works for Fractional but Fails for 0/1 Knapsack
- In **Fractional Knapsack**, unused capacity can always be filled with the best remaining value density. The greedy strategy guarantees 100% capacity utilization with maximum density.
- In **0/1 Knapsack**, items cannot be split. Taking a high-density bulky item may leave empty space that cannot be filled, whereas two lower-density items together might fill the space and provide higher total profit.

---

## C. Complete Code Explanation

### Prescribed Practical Code:
```python
def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_profit = 0

    for profit, weight in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_profit += profit
            capacity -= weight
        else:
            total_profit += profit * capacity / weight
            capacity = 0

    return total_profit


n = int(input("Enter number of items: "))
items = []

for i in range(n):
    profit = float(input("Enter profit: "))
    weight = float(input("Enter weight: "))
    items.append((profit, weight))

capacity = float(input("Enter knapsack capacity: "))

print("Maximum profit:", fractional_knapsack(items, capacity))
```

### Line-by-Line Breakdown:
1. `def fractional_knapsack(items, capacity):`
   - Function accepting a list of tuples `items = [(profit, weight), ...]` and scalar `capacity`.
2. `items.sort(key=lambda x: x[0] / x[1], reverse=True)`:
   - **Crucial Greedy Step:** Sorts the list in-place based on the profit-to-weight ratio `x[0] / x[1]` in descending order (`reverse=True`).
   - Time: $O(n \log n)$ via Python's Timsort.
3. `total_profit = 0`:
   - Accumulator variable tracking the total value of items placed into the knapsack.
4. `for profit, weight in items:`:
   - Loops through each item starting from highest value density.
5. `if capacity == 0: break`:
   - Early termination check: if knapsack is full, stop processing further items.
6. `if weight <= capacity:`:
   - Case 1: Knapsack has sufficient space to take the entire item ($x_i = 1$).
7. `total_profit += profit; capacity -= weight`:
   - Adds full profit to total, decrements knapsack capacity by item's weight.
8. `else:`:
   - Case 2: Knapsack cannot fit the whole item ($weight > capacity$).
9. `total_profit += profit * capacity / weight`:
   - Takes the remaining fraction $x_i = rac{	ext{capacity}}{	ext{weight}}$ of the item. Profit added is $profit 	imes rac{	ext{capacity}}{	ext{weight}}$.
10. `capacity = 0`:
    - Knapsack is now completely full; capacity is set to 0.
11. `return total_profit`:
    - Returns the optimal maximum profit.

### Dry Run with Lab Manual Values:
Input:
Items:
- Item 1: Profit = 12, Weight = 54 $
ightarrow$ Ratio = $12 / 54 pprox 0.222$
- Item 2: Profit = 23, Weight = 43 $
ightarrow$ Ratio = $23 / 43 pprox 0.535$
- Item 3: Profit = 23, Weight = 13 $
ightarrow$ Ratio = $23 / 13 pprox 1.769$
- Capacity $W = 34$

Sorted by Ratio:
1. Item 3: Profit 23, Weight 13 (Ratio 1.769)
2. Item 2: Profit 23, Weight 43 (Ratio 0.535)
3. Item 1: Profit 12, Weight 54 (Ratio 0.222)

Execution:
- Step 1: Examine Item 3. Weight 13 $\le$ Capacity 34.
  - Take whole item: `total_profit` = $0 + 23 = 23$.
  - Remaining capacity = $34 - 13 = 21$.
- Step 2: Examine Item 2. Weight 43 $>$ Remaining capacity 21.
  - Take fraction: $rac{21}{43} pprox 0.48837$.
  - Profit added = $23 	imes rac{21}{43} pprox 11.232558$.
  - New `total_profit` = $23 + 11.232558 = 34.232558$.
  - Remaining capacity = 0.
- Step 3: Capacity is 0. Break loop.
- **Output:** `Maximum profit: 34.23255813953489` (Matches exact lab run!).

---

## D. Algorithm / Pseudocode

```text
Algorithm FractionalKnapsack(P, W, C, n):
1. For i <- 0 to n - 1 do:
     Ratio[i] <- P[i] / W[i]
2. Sort items in non-increasing order of Ratio
3. total_profit <- 0.0
4. For i <- 0 to n - 1 do:
     If C == 0 then
         Break
     If W[i] <= C then:
         total_profit <- total_profit + P[i]
         C <- C - W[i]
     Else:
         total_profit <- total_profit + P[i] * (C / W[i])
         C <- 0
         Break
5. Return total_profit
```

### Complexities:
- **Time Complexity:**
  - Calculating ratios & sorting: $O(n \log n)$.
  - Greedy scan loop: $O(n)$ in the worst case.
  - **Overall Time Complexity:** $O(n \log n)$.
- **Space Complexity:**
  - $O(1)$ auxiliary space if sorted in-place, or $O(n)$ to store item tuples.

---

## E. High-Yield Viva Questions and Answers

**Q1: What is the greedy criterion used in Fractional Knapsack?**
*Answer:* The profit-to-weight ratio ($p_i / w_i$), also known as **value density**.

**Q2: Can we solve 0/1 Knapsack using this exact greedy method?**
*Answer:* No. The greedy strategy fails for 0/1 Knapsack because items cannot be broken; taking a high-ratio item might leave empty space, yielding a suboptimal result.

**Q3: What is the time complexity of the Fractional Knapsack algorithm?**
*Answer:* $O(n \log n)$, dominated by sorting the items by their ratio.

**Q4: Can Fractional Knapsack be solved in $O(n)$ time?**
*Answer:* Yes, theoretically in $O(n)$ time using a **Linear-Time Median of Medians Selection Algorithm** (QuickSelect) to partition items around the median ratio without a full sort.

**Q5: What is the space complexity?**
*Answer:* $O(1)$ auxiliary space beyond the input list.

**Q6: What happens if all items have the same profit-to-weight ratio?**
*Answer:* Any combination of items that completely fills the capacity will give the same optimal maximum profit.

**Q7: What does the variable `x[0] / x[1]` represent in Python?**
*Answer:* `x[0]` is profit and `x[1]` is weight, so the expression computes the value density ratio.

**Q8: What happens if an item has zero weight ($w_i = 0$)?**
*Answer:* A division by zero error (`ZeroDivisionError`) occurs. In practical constraints, item weights are strictly positive ($w_i > 0$).

**Q9: What is the difference between a Feasible Solution and an Optimal Solution?**
*Answer:* A **feasible solution** satisfies the knapsack capacity constraint ($\sum w_i x_i \le W$). An **optimal solution** is a feasible solution that achieves the maximum possible profit.

**Q10: Why does the code check `if capacity == 0: break`?**
*Answer:* As an optimization to avoid unnecessary iterations over remaining items once the knapsack is 100% full.

**Q11: What mathematical property proves the correctness of greedy fractional knapsack?**
*Answer:* The **Greedy Choice Property** and **Optimal Substructure** proven via proof by contradiction (cut-and-paste argument).

**Q12: If you sort by profit only (maximum profit first), does it guarantee optimal result?**
*Answer:* No. A high-profit item might have an enormous weight, leaving no room for other items with far better density.

**Q13: If you sort by weight only (minimum weight first), does it guarantee optimal result?**
*Answer:* No. A light item might have virtually zero profit.

**Q14: What is the range of values for $x_i$ in Fractional Knapsack?**
*Answer:* $0 \le x_i \le 1$.

**Q15: How many items can have a strictly fractional value ($0 < x_i < 1$) in the optimal solution?**
*Answer:* At most **one** item. All preceding chosen items are taken whole ($x_i = 1$), the last fitting item is fractional, and all subsequent items are not taken ($x_i = 0$).

**Q16: How is input read in the practical code?**
*Answer:* Iteratively reading `profit` and `weight` for `n` items, storing them as tuples `(profit, weight)` in a list.

**Q17: Is Fractional Knapsack NP-Complete?**
*Answer:* No, it is in **P** (solvable in polynomial time $O(n \log n)$). The 0/1 Knapsack problem is NP-Complete.

**Q18: What is the difference between `items.sort()` and `sorted(items)`?**
*Answer:* `items.sort()` sorts the list in-place returning `None`, while `sorted(items)` creates and returns a new sorted list.

**Q19: If knapsack capacity is larger than total weight of all items, what happens?**
*Answer:* All items are taken entirely ($x_i = 1$ for all $i$), and the profit is simply the sum of all item profits.

**Q20: Why do we use `reverse=True` in sorting?**
*Answer:* Because standard sorting is ascending (lowest to highest), while the greedy choice requires descending order (highest ratio first).

---

## F. Practical Examination Preparation
- **Must-Remember Lines:**
  - Sorting line: `items.sort(key=lambda x: x[0] / x[1], reverse=True)`
  - Fraction addition: `total_profit += profit * capacity / weight`
- **Execution Checklist:**
  - Remember to convert input to `float` or `int`.
- **Examiner Cross-Question:** "Why can't you use this method for 0-1 knapsack?"
  - *Golden Response:* "Because in 0-1 Knapsack, fractional selection is prohibited. Greedily taking a high-ratio item can leave unusable empty capacity, whereas Dynamic Programming evaluates both inclusion and exclusion to find the global optimum."

---

## G. Quick Revision
1. **Technique:** Greedy Paradigm.
2. **Sorting Key:** Ratio $r_i = rac{p_i}{w_i}$ descending.
3. **Time Complexity:** $O(n \log n)$ (due to sorting).
4. **Space Complexity:** $O(1)$ auxiliary.
5. **Divisibility:** $0 \le x_i \le 1$.
6. **Fractional Items in Optimal Solution:** At most 1 item.
7. **Capacity Utilization:** Always 100% full (if $\sum w_i \ge W$).
8. **Complexity Class:** Belongs to P (Polynomial Time).
9. **0/1 Knapsack Contrast:** Greedy is suboptimal for 0/1; DP is required.
10. **Top Viva Question:** "State the greedy choice property for fractional knapsack and explain why at most one item is fractional."
