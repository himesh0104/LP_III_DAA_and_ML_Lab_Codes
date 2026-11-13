# -*- coding: utf-8 -*-
"""
DAA PRACTICAL 1: FIBONACCI NUMBERS (RECURSIVE VS NON-RECURSIVE)
Savitribai Phule Pune University (SPPU) - LP-III

================================================================================
LAB TEST DEMO DATA TO TYPE IN TERMINAL:
================================================================================
When prompted:
    Enter number of terms [Demo: 8]: 8

(Or simply press ENTER to automatically use the demo value: 8)

Expected Output:
    Non-recursive (Iterative) Fibonacci series:
    0 1 1 2 3 5 8 13

    Recursive Fibonacci series:
    0 1 1 2 3 5 8 13

Complexity Analysis for Lab Evaluation:
    * Non-recursive (Iterative): Time = O(n), Space = O(1)
    * Recursive:                 Time = O(2^n), Space = O(n) call-stack depth
================================================================================
"""

def fib_recursive(n):
    """Calculates n-th Fibonacci number recursively."""
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    """Generates n Fibonacci numbers iteratively."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def main():
    print("=" * 70)
    print(" DAA PRACTICAL 1: FIBONACCI NUMBERS (RECURSIVE VS NON-RECURSIVE)")
    print("=" * 70)
    print("[LAB TEST DEMO DATA: Type 8 and press Enter]")
    print("-" * 70)

    raw_in = input("Enter number of terms [Press Enter for demo: 8]: ").strip()
    n = int(raw_in) if raw_in else 8

    if n <= 0:
        print("Please enter a positive integer.")
        return

    print("\n" + "-" * 70)
    print(f"1. Non-recursive (Iterative) Fibonacci Series ({n} terms):")
    iter_res = fib_iterative(n)
    print("   " + " ".join(map(str, iter_res)))

    print(f"\n2. Recursive Fibonacci Series ({n} terms):")
    rec_res = [fib_recursive(i) for i in range(n)]
    print("   " + " ".join(map(str, rec_res)))

    print("\n" + "=" * 70)
    print("COMPLEXITY ANALYSIS (FOR VIVA / LAB EVALUATION):")
    print("  * Iterative Method: Time Complexity = O(n), Space Complexity = O(1)")
    print("  * Recursive Method: Time Complexity = O(2^n), Space Complexity = O(n)")
    print("=" * 70)

if __name__ == "__main__":
    main()
