# MASTER COMPARISON: ALGORITHMS, COMPLEXITIES & PARADIGMS

## Master Complexity & Paradigm Comparison Table

| Practical | Algorithm | Paradigm | Input Data / Features | Time Complexity (Best / Avg / Worst) | Space Complexity | Key Optimization / Implementation Hook |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **DAA 1 (Rec)** | Fibonacci Numbers | Recursion | Scalar $n$ | $\Omega(2^n) / \Theta(2^n) / O(2^n)$ | $O(n)$ (Stack) | Naive call tree; demonstration of subproblem overlap |
| **DAA 1 (Iter)** | Fibonacci Numbers | Iteration | Scalar $n$ | $\Omega(n) / \Theta(n) / O(n)$ | $O(1)$ | Simultaneous swap `a, b = b, a + b` |
| **DAA 2** | Huffman Encoding | Greedy Method | Characters + Frequencies | $\Omega(n \log n) / \Theta(n \log n) / O(n \log n)$ | $O(n)$ | Min-heap tie-breaking using counter in tuple |
| **DAA 3** | Fractional Knapsack | Greedy Method | Profits, Weights, Capacity | $\Omega(n \log n) / \Theta(n \log n) / O(n \log n)$ | $O(1)$ aux | Sort descending by ratio $p_i / w_i$ |
| **DAA 4** | 0-1 Knapsack | Dynamic Programming | Profits, Weights, Capacity | $\Omega(n \cdot W) / \Theta(n \cdot W) / O(n \cdot W)$ | $O(n \cdot W) \to O(W)$ | Bottom-up 2D tabulation; reverse 1D traversal |
| **DAA 5** | N-Queens | Backtracking | Chessboard size $N$ | $\Omega(N) / \Theta(N!) / O(N!)$ | $O(N^2)$ board, $O(N)$ stack | Check left diagonals and left row only; unmark cell |
| **ML 1 (LR)** | Linear Regression | OLS Regression | `uber.csv` (Coordinates, Time) | $O(n \cdot p^2 + p^3)$ | $O(p)$ | Normal equation closed-form solution |
| **ML 1 (RF)** | Random Forest | Bagged Ensemble | `uber.csv` (Coordinates, Time) | $O(B \cdot n \log n \cdot p')$ | $O(B \cdot \text{nodes})$ | $n\_estimators=100$, feature subspace sampling |
| **ML 2 (KNN)** | K-Nearest Neighbors | Instance-based | `emails.csv` (3000 words) | Train: $O(1)$ \| Test: $O(n \cdot p)$ | $O(n \cdot p)$ | Lazy learning; Euclidean distance voting |
| **ML 2 (SVM)** | Support Vector Machine | Maximum Margin | `emails.csv` (3000 words) | Train: $O(n^2 \cdot p)$ \| Test: $O(n_{sv} \cdot p)$ | $O(n \cdot p)$ | Linear kernel $w^T x + b = 0$; support vectors |
| **ML 3 (MLP)** | Multilayer Perceptron | Deep Learning | `Churn_Modelling.csv` | Train: $O(E \cdot n \cdot \sum n_l n_{l-1})$ | $O(\sum n_l n_{l-1})$ | ReLU, Adam optimizer, L2 alpha=0.01, Early Stopping |
| **ML 4 (KNN)** | K-Nearest Neighbors | Instance-based | `diabetes.csv` (8 clinical features) | Train: $O(1)$ \| Test: $O(n \cdot p)$ | $O(n \cdot p)$ | Median imputation for physiological zero values |
| **ML 5 (KM)** | K-Means Clustering | Centroid Partitioning | `sales_data_sample.csv` | $O(I \cdot n \cdot K \cdot p)$ | $O((n + K) \cdot p)$ | Lloyd's algorithm; k-means++; WCSS / Elbow |
| **ML 5 (HC)** | Agglomerative Clustering | Hierarchical Merging | `sales_data_sample.csv` | $O(n^2 \log n)$ to $O(n^3)$ | $O(n^2)$ | Ward's minimum variance linkage; dendrogram |
