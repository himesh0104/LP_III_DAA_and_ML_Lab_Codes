# DAA ONE-DAY VIVA REVISION GUIDE

## Core Paradigms at a Glance
1. **Divide and Conquer:** Break into non-overlapping subproblems, solve recursively, combine (e.g. Merge Sort).
2. **Greedy Method:** Make locally optimal choice at each step. Fast ($O(n \log n)$), but only works if problem possesses greedy choice property and optimal substructure (Huffman, Fractional Knapsack).
3. **Dynamic Programming:** Solves optimization problems with overlapping subproblems and optimal substructure. Bottom-up tabulation or top-down memoization (0-1 Knapsack).
4. **Backtracking:** DFS traversal on state space tree. Evaluates partial candidates and prunes invalid paths using bounding functions (N-Queens).
5. **Branch and Bound:** BFS / Best-First traversal with priority queue using upper/lower bounds. Designed for discrete combinatorial optimization.

---

## Asymptotic Complexities Summary
| Algorithm | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Fibonacci (Recursive)** | $O(2^n)$ | $O(2^n)$ | $O(2^n)$ | $O(n)$ | Recursion |
| **Fibonacci (Iterative)** | $O(n)$ | $O(n)$ | $O(n)$ | $O(1)$ | Iteration |
| **Huffman Encoding** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Greedy + Min-Heap |
| **Fractional Knapsack** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | Greedy (Density Sort) |
| **0-1 Knapsack (DP)** | $O(n \cdot W)$ | $O(n \cdot W)$ | $O(n \cdot W)$ | $O(n \cdot W)$ or $O(W)$ | Dynamic Programming |
| **N-Queens (Backtracking)** | $O(N)$ | $O(N!)$ | $O(N!)$ | $O(N^2)$ | Backtracking (DFS) |

---

## Rapid-Fire Cross-Questions & Answers
1. *Why is Huffman code prefix-free?* $\rightarrow$ Because characters are strictly placed at the leaf nodes of the binary tree; no leaf can be an ancestor of another leaf!
2. *Why does 0-1 Knapsack fail with Greedy?* $\rightarrow$ Because items are indivisible; leaving empty capacity can result in lower overall profit than a combination of items with lower individual densities.
3. *Why is 0-1 Knapsack pseudo-polynomial?* $\rightarrow$ Because $W$ is a numeric value. Its bit length is $k = \log_2 W$. Time is $O(n \cdot 2^k)$, which is exponential in input bit size.
4. *What happens to 4-Queens with Queen at (0, 0)?* $\rightarrow$ Mathematical dead-end! No solution exists.
5. *How to optimize 0-1 Knapsack space to $O(W)$?* $\rightarrow$ Use a 1D array traversed backwards from $W$ down to $wt_i$ so previous items aren't reused in the same iteration.
