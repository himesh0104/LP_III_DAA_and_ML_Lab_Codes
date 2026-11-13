# DAA Practical 4: 0-1 Knapsack Problem (Dynamic Programming)

## A. Practical Overview
- **Practical Number:** Group A - Practical 4 (Assignment No. 4)
- **Title:** 0-1 Knapsack Problem using Dynamic Programming
- **Aim:** Write a program to solve the 0-1 Knapsack problem using dynamic programming (or branch and bound strategy) and analyze its time and space complexity.
- **Objective:**
  1. Understand the 0/1 (binary inclusion/exclusion) constraint.
  2. Formulate the dynamic programming recurrence relation.
  3. Construct and trace the 2D DP memoization table.
  4. Understand the concept of Pseudo-Polynomial time complexity.
- **What Problem Does This Solve?**
  Given $n$ indivisible items with values $p_i$ and weights $w_i$, and a knapsack of capacity $W$, determine the subset of items to pack such that total weight $\le W$ and total value is maximized. Each item can either be taken completely ($x_i = 1$) or left behind ($x_i = 0$).
- **Why Is This Algorithm Required?**
  A brute-force search evaluates $2^n$ subsets ($O(2^n)$), which is intractable for large $n$. Dynamic programming solves overlapping subproblems efficiently in $O(n \cdot W)$ time.
- **Real-World Applications:**
  - Budget asset allocation and capital budgeting (selecting projects with fixed budgets).
  - Cargo plane loading where packages cannot be broken.
  - Server capacity and VM provisioning with strict memory/CPU limits.

---

## B. Theoretical Foundation
### 1. Mathematical Formulation
Maximize:
$$\sum_{i=1}^n p_i \cdot x_i \quad 	ext{where } x_i \in \{0, 1\}$$
Subject to:
$$\sum_{i=1}^n w_i \cdot x_i \le W$$

### 2. Dynamic Programming State & Recurrence Relation
Let `dp[i][w]` represent the maximum profit achievable using a subset of the first `i` items with a maximum knapsack capacity `w`.

**Base Cases:**
- `dp[0][w] = 0` (0 items available $ightarrow$ profit is 0)
- `dp[i][0] = 0` (capacity is 0 $ightarrow$ profit is 0)

**Recurrence Formula:**
For item $i$ (with weight $w_{i-1}$ and profit $p_{i-1}$ in 0-indexed terms):
- **If item weight exceeds current capacity ($w_{i-1} > w$):**
  Cannot include item $i$:
  $$dp[i][w] = dp[i-1][w]$$
- **If item fits ($w_{i-1} \le w$):**
  We have two choices:
  1. *Exclude item $i$:* Profit is $dp[i-1][w]$.
  2. *Include item $i$:* Profit is $p_{i-1} + dp[i-1][w - w_{i-1}]$.
  Take the maximum:
  $$dp[i][w] = \max(dp[i-1][w], \; p_{i-1} + dp[i-1][w - w_{i-1}])$$

```
DP Table Visualization (n rows x W+1 columns):
        w -> 0   1   2   3 ...  W
i
0           [0   0   0   0 ...  0]
1           [0   .   .   . ...  .]
2           [0   .   .   . ...  .]
...
n           [0   .   .   . ... dp[n][W]] -> Final Answer!
```

---

## C. Complete Code Explanation

### Prescribed Practical Code:
```python
def knapsack(profits, weights, capacity):
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


n = int(input("Enter number of items: "))
profits = []
weights = []

for i in range(n):
    profits.append(int(input("Enter profit: ")))
    weights.append(int(input("Enter weight: ")))


capacity = int(input("Enter knapsack capacity: "))

print("Maximum profit:", knapsack(profits, weights, capacity))
```

### Line-by-Line Breakdown:
1. `def knapsack(profits, weights, capacity):`
   - Defines the function taking lists `profits`, `weights`, and integer `capacity`.
2. `n = len(profits)`:
   - Finds the total count of items.
3. `dp = [[0] * (capacity + 1) for _ in range(n + 1)]`:
   - Allocates a 2D table of dimensions $(n+1) 	imes (	ext{capacity}+1)$ initialized to zeros.
   - **Crucial Python Detail:** Using list comprehension ensures each row is an independent list, preventing shallow copy referencing bugs.
4. `for i in range(1, n + 1):`:
   - Outer loop iterating over items from 1 to $n$.
5. `for w in range(capacity + 1):`:
   - Inner loop iterating over every possible sub-capacity from 0 to `capacity`.
6. `dp[i][w] = dp[i - 1][w]`:
   - Default choice: Exclude the $i$-th item. Profit is carried over from the row above.
7. `if weights[i - 1] <= w:`:
   - Checks if the current item's weight fits inside current sub-capacity `w`.
   - Note: `weights[i - 1]` because `profits` and `weights` are 0-indexed, while DP table is 1-indexed.
8. `dp[i][w] = max(dp[i][w], profits[i - 1] + dp[i - 1][w - weights[i - 1]])`:
   - Updates `dp[i][w]` to the maximum of excluding the item vs. including it ($profit + 	ext{profit with remaining capacity}$).
9. `return dp[n][capacity]`:
   - The bottom-right cell contains the solution for all $n$ items and total capacity `capacity`.

### Dry Run with Lab Manual Values:
Input:
$n = 2$ items
- Item 1: Profit = 43, Weight = 45
- Item 2: Profit = 23, Weight = 13
- Capacity $W = 54$

Execution Trace:
- Initialize table of size $3 	imes 55$ with 0s.
- Row $i = 1$ (Item 1: $P=43, W=45$):
  - For $w < 45$: `dp[1][w] = 0`
  - For $w \ge 45$: `dp[1][w] = max(0, 43 + dp[0][w - 45]) = 43`
- Row $i = 2$ (Item 2: $P=23, W=13$):
  - For $w < 13$: `dp[2][w] = dp[1][w] = 0`
  - For $13 \le w < 45$: `dp[2][w] = max(dp[1][w], 23 + dp[1][w - 13]) = 23`
  - For $45 \le w < 54$: Item 1 gives 43, Item 2 gives 23 $ightarrow \max(43, 23) = 43$.
  - At $w = 54$: Weight needed for both items = $45 + 13 = 58 > 54$. They cannot both fit!
    - Excluding Item 2: `dp[1][54] = 43`
    - Including Item 2: `23 + dp[1][54 - 13] = 23 + dp[1][41] = 23 + 0 = 23`
    - `max(43, 23) = 43`.
- **Output:** `Maximum profit: 43` (Matches exact lab run!).

---

## D. Algorithm / Pseudocode

```text
Algorithm ZeroOneKnapsack(P, Wt, W, n):
1. Create 2D array DP[0...n][0...W] initialized to 0
2. For i <- 1 to n do:
     For w <- 0 to W do:
         DP[i][w] <- DP[i - 1][w]
         If Wt[i - 1] <= w then:
             DP[i][w] <- Max(DP[i][w], P[i - 1] + DP[i - 1][w - Wt[i - 1]])
3. Return DP[n][W]
```

### Complexities:
- **Time Complexity:** $O(n \cdot W)$. There are two nested loops: outer runs $n$ times, inner runs $W+1$ times.
  - *Why Pseudo-Polynomial?* The time is polynomial in the **numeric value** of $W$, but exponential in the **length (number of bits)** of the input $W$ ($\log_2 W$ bits). If $W$ is represented by $k$ bits, $W = 2^k$, making the running time $O(n \cdot 2^k)$.
- **Space Complexity:**
  - Standard 2D table: $O(n \cdot W)$.
  - **Space Optimization:** Can be reduced to $O(W)$ using a 1D array traversed in reverse from $W$ down to $wt_i$.

---

## E. High-Yield Viva Questions and Answers

**Q1: What is the recurrence relation for 0/1 Knapsack?**
*Answer:*
$$dp[i][w] = egin{cases} dp[i-1][w] & 	ext{if } w_{i-1} > w \ \max(dp[i-1][w], \; p_{i-1} + dp[i-1][w - w_{i-1}]) & 	ext{if } w_{i-1} \le w \end{cases}$$

**Q2: Why does the 0/1 Knapsack problem require Dynamic Programming instead of Greedy?**
*Answer:* Because items cannot be divided. Making a locally optimal greedy choice can lead to wasted capacity and a suboptimal global solution. DP exhaustively evaluates both inclusion and exclusion of each item.

**Q3: What are the two essential characteristics of a Dynamic Programming problem?**
*Answer:* **Overlapping Subproblems** (the same subproblems are solved repeatedly) and **Optimal Substructure** (an optimal solution contains optimal solutions to subproblems).

**Q4: Why is the time complexity $O(n \cdot W)$ called "pseudo-polynomial"?**
*Answer:* Because it depends on the magnitude of the number $W$, not just the number of inputs. In computational complexity, input size is measured by the number of bits $k = \log_2 W$. As a function of bit size $k$, the time is $O(n \cdot 2^k)$, which is exponential.

**Q5: Can you optimize the auxiliary space from $O(n \cdot W)$ to $O(W)$? How?**
*Answer:* Yes, because row `i` only depends on the previous row `i-1`. We can use a 1D array `dp[w]` of size $W+1$ and update it in **reverse order** from $w = W$ down to $weights[i]$.

**Q6: Why MUST the 1D space-optimized DP array be traversed in reverse?**
*Answer:* If traversed forward ($0 	o W$), we would use the updated values from the current item $i$ in the same step, effectively allowing the same item to be chosen multiple times (which solves the **Unbounded Knapsack**, not 0/1 Knapsack). Traversing backwards ensures each item is used at most once.

**Q7: How do you backtrack to find which items were actually selected?**
*Answer:* Start at cell $(n, W)$. If `dp[i][w] != dp[i-1][w]`, item $i$ was included; add item $i$ to our list and move to $(i-1, w - weight_{i-1})$. Otherwise, move to $(i-1, w)$. Repeat until $i = 0$.

**Q8: What is the difference between 0/1 Knapsack and Fractional Knapsack?**
*Answer:* In Fractional Knapsack, items are divisible and solved using Greedy method in $O(n \log n)$. In 0/1 Knapsack, items are indivisible ($x_i \in \{0, 1\}$) and solved via DP in $O(n \cdot W)$ or Branch and Bound.

**Q9: What is the Branch and Bound approach for 0/1 Knapsack?**
*Answer:* It uses a state space tree. At each node, it computes an upper bound on profit using the Fractional Knapsack greedy algorithm. If the bound is less than the current best solution, the branch is pruned.

**Q10: Is 0/1 Knapsack NP-Complete?**
*Answer:* Yes, 0/1 Knapsack is NP-Complete (specifically, its decision version is NP-Complete, and the optimization version is NP-Hard).

**Q11: Why is table size `(n + 1)` and `(capacity + 1)`?**
*Answer:* To accommodate base cases: row 0 represents having 0 items available, and column 0 represents having 0 knapsack capacity.

**Q12: What does `dp[i - 1][w - weights[i - 1]]` represent?**
*Answer:* The maximum profit possible with the remaining capacity after subtracting the weight of item $i$, considering only the previous $i-1$ items.

**Q13: What happens if knapsack capacity $W$ is 0?**
*Answer:* The loops complete and return `dp[n][0] = 0`.

**Q14: What happens if all item weights are greater than knapsack capacity $W$?**
*Answer:* No item can fit. The condition `weights[i-1] <= w` never triggers, and the function returns 0.

**Q15: What is the difference between Top-Down Memoization and Bottom-Up Tabulation?**
*Answer:* Top-down uses recursion and caches results in a lookup table on demand. Bottom-up tabulation (used in our code) iteratively fills the DP table starting from the base cases up to the target answer.

**Q16: Which is faster in Python: Tabulation or Memoization?**
*Answer:* Bottom-up tabulation is typically faster in Python because it avoids function call overhead and stack depth limits.

**Q17: Can weights and capacity be floating-point numbers in this DP algorithm?**
*Answer:* No. DP table indexing requires integer capacities and weights. For floating weights, scaling (multiplying by $10^k$) or alternative algorithms (Branch & Bound) are required.

**Q18: What is the worst-case space complexity of Branch and Bound for 0/1 Knapsack?**
*Answer:* $O(2^n)$ in the worst case if no branches are pruned, though on average it explores far fewer states.

**Q19: If profits are [10, 20, 30], weights are [1, 1, 1], capacity is 2, what is max profit?**
*Answer:* Profit is $30 + 20 = 50$ (pick the two items with highest profit).

**Q20: Why do we use `list comprehension` to create the 2D array instead of `[[0]*(W+1)]*(n+1)`?**
*Answer:* `[[0]*(W+1)]*(n+1)` creates shallow copies of the same row; modifying one row would accidentally modify all rows! List comprehension creates independent list objects.

---

## F. Practical Examination Preparation
- **Must-Remember Lines:**
  - Table initialization: `dp = [[0] * (capacity + 1) for _ in range(n + 1)]`
  - Core update:
    ```python
    dp[i][w] = dp[i - 1][w]
    if weights[i - 1] <= w:
        dp[i][w] = max(dp[i][w], profits[i - 1] + dp[i - 1][w - weights[i - 1]])
    ```
- **Execution Checklist:** Make sure inputs are parsed as integers (`int()`).

---

## G. Quick Revision
1. **Technique:** Dynamic Programming (Bottom-Up Tabulation).
2. **State:** `dp[i][w]` = Max profit using first `i` items with capacity `w`.
3. **Time Complexity:** $O(n \cdot W)$ (Pseudo-polynomial).
4. **Space Complexity:** $O(n \cdot W)$, optimizable to $O(W)$.
5. **Item Constraint:** Indivisible ($x_i \in \{0, 1\}$).
6. **NP-Completeness:** Decision version is NP-Complete.
7. **Base Cases:** `dp[0][w] = 0` and `dp[i][0] = 0`.
8. **1D Optimization Rule:** Loop backwards from $W$ down to $wt_i$ to prevent multiple uses of the same item.
9. **Branch & Bound Alternative:** Prunes branches using fractional knapsack upper bounds.
10. **Top Viva Question:** "Write down the DP recurrence relation for 0/1 Knapsack and explain why its time complexity is called pseudo-polynomial."
