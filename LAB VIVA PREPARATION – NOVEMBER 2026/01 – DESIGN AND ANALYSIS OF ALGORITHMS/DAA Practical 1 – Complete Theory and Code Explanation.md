# DAA Practical 1: Fibonacci Numbers (Recursive vs. Non-Recursive)

## A. Practical Overview
- **Practical Number:** Group A - Practical 1 (Assignment No. 1)
- **Title:** Fibonacci Numbers Calculation and Complexity Analysis
- **Aim:** Write a program (both non-recursive and recursive) to calculate Fibonacci numbers and analyze their time and space complexity.
- **Objective:**
  1. Understand the mathematical properties and recurrence relation of the Fibonacci sequence.
  2. Implement iterative (non-recursive) and recursive approaches in Python.
  3. Compare and analyze the time complexity and auxiliary space complexity of both techniques.
- **What Problem Does This Solve?**
  Generating terms in the integer sequence $0, 1, 1, 2, 3, 5, 8, 13, 21, \dots$ where each term is the sum of the two preceding terms. It serves as the quintessential benchmark problem in computer science to demonstrate the danger of overlapping subproblems in naive recursion versus the efficiency of iterative state tracking.
- **Why Is This Algorithm Required?**
  Computing Fibonacci numbers is foundational to understanding algorithm design paradigms (Divide & Conquer vs. Dynamic Programming / Iteration) and analyzing recurrence relations.
- **Real-World Applications:**
  - Financial modeling and Fibonacci retracement levels in stock market technical analysis.
  - Computer graphics, generative art, and phyllotaxis (modeling biological patterns in sunflowers, pinecones).
  - Advanced data structures such as **Fibonacci Heaps**, which achieve $O(1)$ amortized insertion and decrease-key time.
  - Fibonacci Search technique for sorted arrays.

---

## B. Theoretical Foundation
### 1. Mathematical Definition
The Fibonacci sequence $F_n$ is defined by the linear recurrence relation:
$$F_0 = 0, \quad F_1 = 1$$
$$F_n = F_{n-1} + F_{n-2} \quad 	ext{for } n \ge 2$$

### 2. Recurrence Relation & Recursion Tree
For the recursive algorithm `fib_recursive(n)`:
$$T(n) = T(n-1) + T(n-2) + O(1)$$
Solving this recurrence gives an upper bound of $O(2^n)$ or tight bound $\Theta(\phi^n)$ where $\phi = rac{1+\sqrt{5}}{2} pprox 1.618$ (The Golden Ratio).

```
Recursion Tree for fib(5):
                         fib(5)
                     /            \
              fib(4)                fib(3)
             /      \              /      \
        fib(3)      fib(2)       fib(2)    fib(1)
       /     \     /    \       /    \
   fib(2)  fib(1) fib(1) fib(0) fib(1) fib(0)
   /    \
fib(1) fib(0)
```
**Observation:** `fib(3)` is computed 2 times, `fib(2)` is computed 3 times, `fib(1)` is computed 5 times! This exponential blowup is caused by **overlapping subproblems**.

### 3. Iterative (Non-Recursive) Working Principle
Instead of top-down tree branching, the iterative method uses bottom-up state progression with two variables `a` and `b`. At each step, `a` becomes `b`, and `b` becomes `a + b`. It computes each term exactly once.

### 4. Comparison Summary
| Metric | Recursive Approach | Iterative (Non-Recursive) Approach |
| :--- | :--- | :--- |
| **Time Complexity** | $O(2^n)$ (Exponential) | $O(n)$ (Linear) |
| **Auxiliary Space** | $O(n)$ (Call stack frames) | $O(1)$ (Only two variables `a, b`) |
| **Overlapping Subproblems** | Recomputes identical subproblems repeatedly | Computes each subproblem exactly once |
| **Risk of Stack Overflow** | High for $n > 1000$ (`RecursionError`) | None (constrained only by system RAM) |

---

## C. Complete Code Explanation

### Prescribed Practical Code:
```python
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


n = int(input("Enter number of terms: "))

print("Non-recursive Fibonacci:")
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print("\nRecursive Fibonacci:")
for i in range(n):
    print(fib_recursive(i), end=" ")
```

### Line-by-Line Breakdown:
1. `def fib_recursive(n):`
   - Defines a recursive function that takes an integer `n` and returns the $n$-th Fibonacci number.
2. `if n <= 1:`
   - **Base condition**: In recursion, a termination condition is mandatory. If $n = 0$, returns 0; if $n = 1$, returns 1.
3. `return n`
   - Directly returns $n$ for the base cases (0 or 1).
4. `return fib_recursive(n - 1) + fib_recursive(n - 2)`
   - **Recursive step**: Calls itself for the two preceding values and adds them. This branches into two calls per level, causing the binary recursion tree.
5. `n = int(input("Enter number of terms: "))`
   - Reads the number of terms to generate from standard input and casts it to an integer.
6. `print("Non-recursive Fibonacci:")`
   - Header for the iterative output.
7. `a, b = 0, 1`
   - Initializes the first two Fibonacci numbers: $F_0 = 0, F_1 = 1$.
8. `for i in range(n):`
   - Loop executes exactly $n$ times ($i = 0, 1, \dots, n-1$).
9. `print(a, end=" ")`
   - Prints the current Fibonacci number `a` on the same line followed by a space.
10. `a, b = b, a + b`
    - Simultaneous tuple assignment in Python:
      - New `a` gets the old value of `b`.
      - New `b` gets the sum of old `a` and old `b`.
      - **Crucial Viva Detail:** This avoids using a temporary variable `temp = a; a = b; b = temp + b;`.
11. `print("\nRecursive Fibonacci:")`
    - Prints a newline and the header for recursive output.
12. `for i in range(n):`
    - Iterates $i$ from 0 to $n-1$.
13. `print(fib_recursive(i), end=" ")`
    - Calls `fib_recursive(i)` to compute and print the $i$-th Fibonacci number.
    - **Total Time in this loop:** Since computing term $i$ takes $O(2^i)$, summing over $i=0$ to $n-1$ takes $\sum_{i=0}^{n-1} 2^i = 2^n - 1 = O(2^n)$.

### Dry Run with $n = 5$:
- **Non-recursive trace:**
  - Start: `a = 0, b = 1`
  - $i=0$: print `0`; update `a = 1, b = 0 + 1 = 1`
  - $i=1$: print `1`; update `a = 1, b = 1 + 1 = 2`
  - $i=2$: print `1`; update `a = 2, b = 1 + 2 = 3`
  - $i=3$: print `2`; update `a = 3, b = 2 + 3 = 5`
  - $i=4$: print `3`; update `a = 5, b = 3 + 5 = 8`
  - Output: `0 1 1 2 3`

---

## D. Algorithm / Pseudocode

### 1. Iterative Algorithm:
```text
Algorithm IterativeFibonacci(n):
1. If n <= 0, Return
2. Set a <- 0, b <- 1
3. For i <- 0 to n - 1 do:
     Print a
     Set next_term <- a + b
     Set a <- b
     Set b <- next_term
4. End
```

### 2. Recursive Algorithm:
```text
Algorithm RecursiveFib(n):
1. If n == 0, Return 0
2. If n == 1, Return 1
3. Return RecursiveFib(n - 1) + RecursiveFib(n - 2)
```

---

## E. High-Yield Viva Questions and Answers

**Q1: What is the recurrence relation for the recursive Fibonacci algorithm?**
*Answer:* $T(n) = T(n-1) + T(n-2) + O(1)$, which yields a time complexity of $O(2^n)$ or $\Theta(1.618^n)$.

**Q2: Why is the recursive algorithm so inefficient compared to the iterative one?**
*Answer:* Because of **overlapping subproblems**. The recursive function recalculates the exact same values multiple times across different branches of the call tree without caching them.

**Q3: What is the space complexity of the recursive Fibonacci function and why?**
*Answer:* $O(n)$ auxiliary space. Even though there are $O(2^n)$ total calls, the maximum depth of the call stack at any one instant is equal to $n$.

**Q4: What is the space complexity of the non-recursive Fibonacci function?**
*Answer:* $O(1)$ (constant space), because it only retains two scalar variables (`a` and `b`) regardless of $n$.

**Q5: What happens if we pass $n = 50$ to the recursive function?**
*Answer:* The program will freeze or take an extremely long time (hours/days) because $2^{50} pprox 10^{15}$ operations are required.

**Q6: What happens if we pass $n = 2000$ to the recursive function in Python?**
*Answer:* It raises `RecursionError: maximum recursion depth exceeded in comparison` because Python's default stack limit is 1000.

**Q7: How does `a, b = b, a + b` work in Python?**
*Answer:* Python evaluates the right-hand side expression as an ephemeral tuple `(b, a + b)` before unpacking and assigning the values to `a` and `b`, eliminating the need for a temporary variable.

**Q8: Can we optimize the recursive Fibonacci function without rewriting it as a loop?**
*Answer:* Yes, using **Memoization** (Top-Down Dynamic Programming) or Python's `@functools.lru_cache()`, which caches computed results, reducing the time complexity to $O(n)$.

**Q9: What is the fastest known algorithm to compute the $n$-th Fibonacci number?**
*Answer:* **Matrix Exponentiation** using binary exponentiation on $egin{pmatrix} 1 & 1 \ 1 & 0 \end{pmatrix}^n$, running in $O(\log n)$ time and $O(\log n)$ or $O(1)$ space.

**Q10: What is Binet's Formula? Why do we avoid it in computer programs for large $n$?**
*Answer:* Binet's formula is $F_n = rac{1}{\sqrt{5}} \left( \left(rac{1+\sqrt{5}}{2}ight)^n - \left(rac{1-\sqrt{5}}{2}ight)^n ight)$. We avoid it for large $n$ because floating-point precision limits cause round-off errors.

**Q11: What is the difference between Time Complexity and Execution Time?**
*Answer:* Time complexity is an asymptotic measure of how operation count scales with input size $n$ independent of hardware. Execution time is actual wall-clock duration dependent on CPU speed, OS scheduling, and memory.

**Q12: In the recursive output loop, what is the total time complexity to print $n$ terms?**
*Answer:* $\sum_{i=0}^{n-1} O(2^i) = O(2^n)$. It is still exponential.

**Q13: Why is base condition mandatory in recursion?**
*Answer:* Without a base condition, the function calls itself indefinitely until the call stack memory is exhausted, resulting in a stack overflow error.

**Q14: Is Fibonacci calculation a Divide and Conquer problem?**
*Answer:* It divides the problem into subproblems, but it is NOT an efficient Divide and Conquer algorithm because the subproblems are overlapping, not independent.

**Q15: How can you increase the recursion limit in Python?**
*Answer:* Using `sys.setrecursionlimit(limit)`.

**Q16: What is Tail Recursion? Is `fib_recursive` tail recursive?**
*Answer:* A recursive call is tail recursive if it is the very last operation executed in the function. `fib_recursive` is NOT tail recursive because it must perform an addition `+` after both recursive calls return.

**Q17: Does Python optimize tail recursion?**
*Answer:* No, Python does not support Tail Call Optimization (TCO) by design to preserve complete stack traces for debugging.

**Q18: What is the Golden Ratio and how does it relate to Fibonacci?**
*Answer:* The ratio of consecutive Fibonacci numbers $\lim_{n 	o \infty} rac{F_{n+1}}{F_n} = \phi = rac{1+\sqrt{5}}{2} pprox 1.6180339887\dots$

**Q19: If an examiner asks you to calculate $F_7$ verbally, what is it?**
*Answer:* Sequence: $F_0=0, F_1=1, F_2=1, F_3=2, F_4=3, F_5=5, F_6=8, F_7=13$.

**Q20: Why does the non-recursive loop use `range(n)`?**
*Answer:* To generate exactly $n$ terms starting from index 0 up to $n-1$.

---

## F. Practical Examination Preparation
- **Must-Remember Lines:**
  - Recursive base check: `if n <= 1: return n`
  - Recursive call: `return fib_recursive(n - 1) + fib_recursive(n - 2)`
  - Simultaneous update: `a, b = b, a + b`
- **Safe Modifications:** You can prompt for a single $n$-th number or loop to print a series. If asked to use a `while` loop:
  ```python
  count = 0
  while count < n:
      print(a, end=" ")
      a, b = b, a + b
      count += 1
  ```
- **What Happens If Condition Changes?**
  - If base case is `if n == 0: return 0`, then `fib_recursive(1)` will call `fib_recursive(0) + fib_recursive(-1)`, leading to infinite negative recursion and immediate crash!
- **Examiner Defense Strategy:** Emphasize that the lab purpose is to demonstrate why naive recursion fails on overlapping subproblems ($O(2^n)$ vs $O(n)$).

---

## G. Quick Revision
1. **Mathematical formula:** $F_n = F_{n-1} + F_{n-2}$, with $F_0 = 0, F_1 = 1$.
2. **Recursive Time:** $O(2^n)$ (Exponential).
3. **Recursive Space:** $O(n)$ (Stack frames depth).
4. **Iterative Time:** $O(n)$ (Linear).
5. **Iterative Space:** $O(1)$ (Constant auxiliary memory).
6. **Core cause of recursive slowdown:** Redundant evaluation of overlapping subproblems.
7. **Python tuple trick:** `a, b = b, a + b` evaluates RHS before updating LHS.
8. **Base condition:** `if n <= 1: return n` prevents infinite recursion.
9. **Memoization:** Caching subproblem outputs converts recursive time from $O(2^n)$ to $O(n)$.
10. **Most Probable Viva Question:** "Why does recursive Fibonacci have exponential time complexity while the iterative version is linear?"
