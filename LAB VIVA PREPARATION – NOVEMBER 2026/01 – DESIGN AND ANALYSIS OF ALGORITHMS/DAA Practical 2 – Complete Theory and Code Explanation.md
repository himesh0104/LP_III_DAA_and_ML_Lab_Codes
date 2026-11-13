# DAA Practical 2: Huffman Encoding Using Greedy Strategy

## A. Practical Overview
- **Practical Number:** Group A - Practical 2 (Assignment No. 2)
- **Title:** Huffman Encoding using Greedy Strategy
- **Aim:** Write a program to implement Huffman Encoding using a greedy strategy and analyze its time and space complexity.
- **Objective:**
  1. Understand the principles of lossless data compression.
  2. Implement a Min-Heap (Priority Queue) to build an optimal prefix tree.
  3. Generate variable-length binary prefix codes for characters based on their frequencies.
  4. Analyze the greedy choice property and optimal substructure.
- **What Problem Does This Solve?**
  In standard fixed-length encoding (like ASCII, which uses 8 bits per character), a message of 1,000 characters always requires 8,000 bits. Huffman encoding assigns shorter bit sequences to frequently occurring characters and longer sequences to rare characters, drastically reducing the total number of bits required without losing any data.
- **Why Is This Algorithm Required?**
  It is the optimal greedy algorithm for constructing prefix-free codes, saving between 20% to 70% storage/bandwidth.
- **Real-World Applications:**
  - File compression tools like **GZIP**, **ZIP**, and **PKZIP**.
  - Multimedia standards including **JPEG** image compression and **MP3** audio encoding.
  - Network transmission protocols and data serialization.

---

## B. Theoretical Foundation
### 1. Lossless Compression & Variable-Length Codes
- **Lossless Compression:** The original data can be perfectly reconstructed from the compressed bits with zero error.
- **Fixed-Length vs. Variable-Length:** If we have 4 characters (A, B, C, D), fixed-length needs 2 bits each (00, 01, 10, 11). If 'A' occurs 90% of the time, variable-length can assign 'A' = '0' (1 bit), significantly cutting file size.

### 2. The Prefix Rule (Prefix-Free Codes)
No assigned code may be a prefix of any other code.
- *Example of ambiguous code (Invalid):* If A='0', B='1', C='01'. In a bitstream `01`, the decoder cannot tell whether it is `AB` or `C`.
- *Huffman Prefix-Free:* If A='0', B='10', C='11', the bitstream `01011` can ONLY be parsed as `0` (A), `10` (B), `11` (C) -> `ABC`. No delimiters are required!

### 3. Greedy Choice & Min-Heap Working Principle
1. Count character frequencies.
2. Insert all characters as leaf nodes into a **Min-Priority Queue** (Min-Heap keyed by frequency).
3. Repeatedly extract the two nodes with the lowest frequencies: $f_1$ and $f_2$.
4. Create a new parent node with frequency $f_1 + f_2$, assigning the two nodes as left and right children.
5. Insert the new internal node back into the Min-Heap.
6. Repeat until exactly one root node remains. This root represents the complete Huffman Tree.
7. Traverse the tree from root: assigning `0` to left edges and `1` to right edges.

```
Example Tree Construction for (a:5, b:2, c:1, d:1):
Step 1: Min-heap has [c:1, d:1, b:2, a:5]
Step 2: Combine c:1 and d:1 -> (cd:2)
        Heap has [b:2, cd:2, a:5]
Step 3: Combine b:2 and cd:2 -> (bcd:4)
        Heap has [bcd:4, a:5]
Step 4: Combine bcd:4 and a:5 -> (Root:9)

Tree Structure:
             Root (9)
            /        \
        [0]/          \[1]
      bcd (4)         a (5) -> Code: "1"
      /     \
  [0]/       \[1]
   b (2)     cd (2) -> Code for b: "00"
             /    \
         [0]/      \[1]
          c (1)    d (1) -> Code for c: "010", d: "011"
```

---

## C. Complete Code Explanation

### Prescribed Practical Code:
```python
import heapq

def huffman(characters, frequencies):
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
            print(node, ":", code if code else "0")
            return

        left, right = node
        print_codes(left, code + "0")
        print_codes(right, code + "1")

    if heap:
        print("Huffman Codes:")
        print_codes(heap[0][2])


n = int(input("Enter number of characters: "))
characters = []
frequencies = []

for i in range(n):
    ch = input("Enter character: ")
    freq = int(input("Enter frequency: "))
    characters.append(ch)
    frequencies.append(freq)

huffman(characters, frequencies)
```

### Line-by-Line Breakdown:
1. `import heapq`:
   - Imports Python's built-in binary heap algorithm module providing $O(\log n)$ push and pop operations on lists.
2. `def huffman(characters, frequencies):`
   - Defines the main Huffman encoding function taking parallel lists of characters and their frequencies.
3. `heap = []`:
   - Initializes an empty list to serve as the min-heap.
4. `for i in range(len(characters)):`
   - Iterates through all input characters.
5. `heapq.heappush(heap, (frequencies[i], i, characters[i]))`:
   - Pushes a 3-element tuple `(frequency, tie_breaker_index, character)` into the min-heap.
   - **Crucial Viva Insight:** Why include `i`? In Python 3, if two elements have identical frequencies, Python compares the next tuple element. Without `i`, it would try to compare character or tree nodes directly, which triggers a `TypeError` when nodes are non-comparable tuples. The index `i` guarantees unique tie-breaking!
6. `counter = len(characters)`:
   - Initializes an incrementing counter for internal combined nodes, ensuring subsequent tie-breakers are also strictly unique.
7. `while len(heap) > 1:`
   - Continues merging until only 1 root node remains in the heap.
8. `f1, _, left = heapq.heappop(heap)`:
   - Extracts the node with the lowest frequency from the min-heap.
9. `f2, _, right = heapq.heappop(heap)`:
   - Extracts the node with the second lowest frequency.
10. `node = (left, right)`:
    - Creates a binary tree branch tuple where `left` and `right` are children.
11. `heapq.heappush(heap, (f1 + f2, counter, node))`:
    - Inserts the combined node back into the min-heap with combined frequency `f1 + f2` and new unique `counter`.
12. `counter += 1`:
    - Increments the unique tie-breaker counter.
13. `def print_codes(node, code=""):`
    - Helper recursive function to traverse the generated tree and print prefix codes.
14. `if isinstance(node, str):`:
    - **Base condition**: If the node is a `str`, it is a leaf character.
15. `print(node, ":", code if code else "0")`:
    - Prints the character and its accumulated binary code. If there was only 1 character in total, defaults to `"0"`.
16. `left, right = node`:
    - Unpacks internal node into left and right subtrees.
17. `print_codes(left, code + "0")`:
    - Recursive call traversing left branch, appending `'0'` to the code string.
18. `print_codes(right, code + "1")`:
    - Recursive call traversing right branch, appending `'1'` to the code string.
19. `if heap:` / `print_codes(heap[0][2])`:
    - Initiates traversal from the tree root stored in `heap[0][2]`.

---

## D. Algorithm / Pseudocode

```text
Algorithm HuffmanEncoding(C, F, n):
1. Q <- Empty Min-Priority Queue
2. For i <- 0 to n - 1 do:
     Create node z where z.char = C[i], z.freq = F[i], z.left = NULL, z.right = NULL
     Insert z into Q
3. For i <- 1 to n - 1 do:
     Allocate new node z
     z.left <- Extract-Min(Q)
     z.right <- Extract-Min(Q)
     z.freq <- z.left.freq + z.right.freq
     Insert z into Q
4. Return Extract-Min(Q)  // Root of the Huffman Tree
```

### Complexities:
- **Time Complexity:**
  - Building initial heap with $n$ elements: $O(n)$ using heapify or $O(n \log n)$ via successive pushes.
  - While loop runs $n-1$ times. In each iteration, 2 `heappop` and 1 `heappush` take $O(\log n)$. Merging takes $(n-1) 	imes 3 \log n = O(n \log n)$.
  - Tree traversal takes $O(n)$ to visit all nodes.
  - **Overall Time Complexity:** $O(n \log n)$.
  - *Special Case:* If input frequencies are already sorted, we can build the tree in $O(n)$ time using two FIFO queues.
- **Space Complexity:**
  - Tree nodes: $2n - 1$ total nodes = $O(n)$.
  - Heap storage: $O(n)$.
  - Recursion stack: $O(	ext{height of tree}) = O(n)$ worst-case, $O(\log n)$ balanced.
  - **Overall Space Complexity:** $O(n)$.

---

## E. High-Yield Viva Questions and Answers

**Q1: What paradigm does Huffman Coding follow?**
*Answer:* Greedy Paradigm. It makes the locally optimal choice at each step (merging the two least frequent nodes) to achieve a globally optimal prefix tree.

**Q2: What is a prefix-free code?**
*Answer:* A code system in which no valid code word is a prefix of any other valid code word, allowing unambiguous decoding without separator symbols.

**Q3: What is the purpose of `counter` in `(f1 + f2, counter, node)`?**
*Answer:* It serves as an integer tie-breaker for the min-heap. If two nodes have identical frequencies, Python compares `counter`, preventing a `TypeError` from comparing non-comparable nested tuples.

**Q4: What data structure is used to implement Huffman's greedy choice efficiently?**
*Answer:* A **Min-Heap** (Priority Queue), which allows retrieving the minimum frequency elements in $O(\log n)$ time.

**Q5: What is the overall time complexity of Huffman Coding for $n$ distinct characters?**
*Answer:* $O(n \log n)$ because there are $n-1$ merges, each performing heap operations of cost $O(\log n)$.

**Q6: Can Huffman coding be achieved in $O(n)$ time?**
*Answer:* Yes, if the input characters and frequencies are already sorted, we can use two standard queues (one for leaf nodes and one for merged nodes) to achieve linear $O(n)$ time.

**Q7: How many total nodes are in a Huffman tree for $n$ leaf characters?**
*Answer:* Exactly $2n - 1$ nodes ($n$ leaves and $n - 1$ internal merge nodes).

**Q8: Is the Huffman tree always a full binary tree?**
*Answer:* Yes, every internal node has strictly two children (degree 2) because we always combine exactly two nodes at each step.

**Q9: If character 'E' has frequency 50% and 'Z' has 1%, which one gets the longer code?**
*Answer:* 'Z' gets the longer code because it is pushed further down the tree during merges, while 'E' stays near the top and gets a short code.

**Q10: Is the generated Huffman code unique?**
*Answer:* No, the codes are not strictly unique because assigning 0 to left vs right is arbitrary, and equal frequencies can be ordered differently. However, the **expected code length** is always identical and optimal.

**Q11: How does decompression (decoding) work in Huffman coding?**
*Answer:* Read the compressed bitstream bit by bit, moving left on '0' and right on '1' from the root of the Huffman tree. When a leaf is reached, output the character and return to the root.

**Q12: What is the optimal substructure property in Huffman coding?**
*Answer:* The optimal tree for an alphabet $C$ can be constructed by replacing two least frequent characters $x, y$ with a merged character $z$, finding the optimal tree for $C' = (C - \{x, y\}) \cup \{z\}$, and replacing $z$ with $x$ and $y$.

**Q13: What happens if all characters have equal frequencies?**
*Answer:* The tree becomes a balanced binary tree, and all characters receive codes of approximately equal length ($\lceil \log_2 n ceil$ bits), behaving like a fixed-length code.

**Q14: What is the difference between static and adaptive Huffman coding?**
*Answer:* Static Huffman calculates frequencies beforehand over the entire text and transmits the tree. Adaptive (dynamic) Huffman updates the tree on the fly as characters are streamed without prior frequency scanning.

**Q15: What is the worst-case shape of a Huffman tree?**
*Answer:* A skewed tree (like a linked list) of height $n-1$, which occurs when frequencies follow Fibonacci numbers.

**Q16: Why is Huffman code called lossless?**
*Answer:* Because the decompression process reconstructs the exact original bitstream with 100% fidelity; no information is discarded.

**Q17: Why do we use `heapq.heappop` twice in the loop?**
*Answer:* To extract the two smallest elements in the priority queue to merge them.

**Q18: What is entropy in information theory, and what is its relation to Huffman coding?**
*Answer:* Shannon's entropy $H = -\sum p_i \log_2 p_i$ represents the theoretical lower bound on average code length. Huffman coding produces an average code length $L$ such that $H \le L < H + 1$.

**Q19: If there is only 1 character in the input, what does the code output?**
*Answer:* The code outputs `"0"` because of the condition `code if code else "0"`.

**Q20: What is the difference between Huffman and Shannon-Fano coding?**
*Answer:* Shannon-Fano is top-down (divides list into two parts of equal total frequency) and is not always optimal. Huffman is bottom-up (merges two lowest frequencies) and is mathematically proven to be optimal.

---

## F. Practical Examination Preparation
- **Must-Remember Lines:**
  - `import heapq`
  - Push tuple: `heapq.heappush(heap, (frequencies[i], i, characters[i]))`
  - While loop: `while len(heap) > 1:`
  - Merging: `f1, _, left = heapq.heappop(heap)`
  - Re-pushing: `heapq.heappush(heap, (f1 + f2, counter, (left, right)))`
- **Examiner Trap:** "Why did you put `i` and `counter` in the tuple?" -> Answer immediately: "To break ties and prevent Python from trying to compare nested tree tuples."
- **Execution Test:** Test with 2 characters: `a: 5`, `b: 2`. Output: `b: 0`, `a: 1`.

---

## G. Quick Revision
1. **Technique:** Greedy Method + Min-Heap.
2. **Time Complexity:** $O(n \log n)$.
3. **Space Complexity:** $O(n)$.
4. **Key Property:** Prefix-free codes (no code is a prefix of another).
5. **Tree Structure:** Full binary tree with $2n - 1$ total nodes.
6. **Rule:** Left edge = '0', Right edge = '1'.
7. **High Frequency:** Placed near tree root $ightarrow$ shorter code.
8. **Low Frequency:** Placed deep in tree $ightarrow$ longer code.
9. **Tie-Breaker:** Numerical index prevents tuple comparison error.
10. **Top Viva Question:** "Why is Huffman coding prefix-free and what data structure makes it $O(n \log n)$?"
