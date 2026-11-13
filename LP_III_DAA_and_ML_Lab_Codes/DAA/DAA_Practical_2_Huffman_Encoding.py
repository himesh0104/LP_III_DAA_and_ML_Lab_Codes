# -*- coding: utf-8 -*-
"""
DAA PRACTICAL 2: HUFFMAN ENCODING (GREEDY STRATEGY)
Savitribai Phule Pune University (SPPU) - LP-III

================================================================================
LAB TEST DEMO DATA TO TYPE IN TERMINAL:
================================================================================
Standard 6-Character Textbook Demo:
    Enter number of characters [Demo: 6]: 6
    Enter character 1: a
    Enter frequency for 'a': 5
    Enter character 2: b
    Enter frequency for 'b': 9
    Enter character 3: c
    Enter frequency for 'c': 12
    Enter character 4: d
    Enter frequency for 'd': 13
    Enter character 5: e
    Enter frequency for 'e': 16
    Enter character 6: f
    Enter frequency for 'f': 45

(Or simply press ENTER at the first prompt to auto-load all 6 characters!)

Expected Output:
    f : 0
    c : 100
    d : 101
    a : 1100
    b : 1101
    e : 111

Complexity Analysis:
    * Time Complexity:  O(n log n) using Min-Heap
    * Space Complexity: O(n) for binary tree nodes and heap
================================================================================
"""
import heapq

def huffman(characters, frequencies):
    """Builds Huffman Tree using Min-Heap and returns a dict of prefix codes."""
    heap = []
    # Push tuples: (frequency, counter, node)
    for i in range(len(characters)):
        heapq.heappush(heap, (frequencies[i], i, characters[i]))

    counter = len(characters)
    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        node = (left, right)
        heapq.heappush(heap, (f1 + f2, counter, node))
        counter += 1

    codes = {}
    def get_codes(node, code=""):
        if isinstance(node, str):
            codes[node] = code if code else "0"
            return
        left, right = node
        get_codes(left, code + "0")
        get_codes(right, code + "1")

    if heap:
        get_codes(heap[0][2])
    return codes

def main():
    print("=" * 70)
    print(" DAA PRACTICAL 2: HUFFMAN ENCODING (GREEDY STRATEGY)")
    print("=" * 70)
    print("[LAB TEST DEMO DATA: 6 characters -> a:5, b:9, c:12, d:13, e:16, f:45]")
    print("-" * 70)

    raw_n = input("Enter number of characters [Press Enter for demo: 6]: ").strip()
    if not raw_n:
        print(">> Auto-loading Standard Demo Dataset (6 characters: a, b, c, d, e, f)...")
        characters = ['a', 'b', 'c', 'd', 'e', 'f']
        frequencies = [5, 9, 12, 13, 16, 45]
    else:
        n = int(raw_n)
        characters = []
        frequencies = []
        for i in range(n):
            ch = input(f"  Enter character {i+1}: ").strip()
            fr = int(input(f"  Enter frequency for '{ch}': ").strip())
            characters.append(ch)
            frequencies.append(fr)

    codes = huffman(characters, frequencies)

    print("\n" + "=" * 70)
    print("GENERATED HUFFMAN CODES (PREFIX-FREE ENCODING):")
    print("-" * 70)
    print(f"{'Character':<15}{'Frequency':<15}{'Huffman Code':<15}")
    print("-" * 70)
    for ch, fr in zip(characters, frequencies):
        print(f"{ch:<15}{fr:<15}{codes.get(ch, ''):<15}")

    orig_bits = sum(frequencies) * 8
    comp_bits = sum(fr * len(codes[ch]) for ch, fr in zip(characters, frequencies))
    print("-" * 70)
    print(f"Uncompressed Size (ASCII 8-bit): {orig_bits} bits")
    print(f"Compressed Huffman Size:         {comp_bits} bits")
    print(f"Total Bit Savings:               {orig_bits - comp_bits} bits ({(orig_bits - comp_bits)/orig_bits*100:.2f}%)")
    print("=" * 70)
    print("COMPLEXITY ANALYSIS:")
    print("  * Time Complexity:  O(n log n)")
    print("  * Space Complexity: O(n)")
    print("=" * 70)

if __name__ == "__main__":
    main()
