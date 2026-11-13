# TOP 50 EXPECTED VIVA QUESTIONS & INSTANT SPOKEN ANSWERS

### DAA Top 25
1. **What is an algorithm?** -> A finite, step-by-step, unambiguous set of instructions to solve a given problem.
2. **What is Big-O notation?** -> Asymptotic upper bound describing the worst-case rate of growth of an algorithm.
3. **What is Omega and Theta notation?** -> Omega ($\Omega$) is asymptotic lower bound (best-case); Theta ($\Theta$) is asymptotically tight bound.
4. **Why is recursive Fibonacci exponential?** -> Due to repeated recomputation of overlapping subproblems in a binary call tree.
5. **What is auxiliary space?** -> Temporary extra memory used by an algorithm, excluding the memory taken by the input itself.
6. **What is the space complexity of recursive Fibonacci?** -> $O(n)$ due to maximum call stack depth.
7. **What is a prefix-free code?** -> A code where no codeword is a prefix of any other, enabling unambiguous decoding.
8. **What data structure powers Huffman coding?** -> Min-Priority Queue (Min-Heap), giving $O(\log n)$ extraction.
9. **How many nodes in a Huffman tree for $n$ leaves?** -> Exactly $2n - 1$ total nodes ($n$ leaves and $n-1$ internal nodes).
10. **What is the greedy choice in Fractional Knapsack?** -> Value density: profit-to-weight ratio ($p_i / w_i$) in descending order.
11. **Can more than one item be fractional in Fractional Knapsack?** -> No, at most one item is fractional.
12. **Why does greedy fail on 0-1 Knapsack?** -> Indivisibility leaves wasted capacity that could have yielded higher total profit.
13. **What are the two prerequisites for Dynamic Programming?** -> Overlapping subproblems and optimal substructure.
14. **What is the recurrence relation for 0-1 Knapsack?** -> $dp[i][w] = \max(dp[i-1][w], \; p_{i-1} + dp[i-1][w - w_{i-1}])$.
15. **What does pseudo-polynomial mean?** -> Polynomial in numeric value of input, but exponential in bit-length of input ($O(n \cdot 2^k)$).
16. **How to reduce 0-1 Knapsack space to $O(W)$?** -> Use a 1D array iterated in reverse from $W$ down to $wt_i$.
17. **What is Backtracking?** -> Depth-First Search with bounding functions to prune non-viable candidate solutions.
18. **What is a Bounding Function?** -> A predicate test (`is_safe`) that determines if a partial solution can be completed safely.
19. **Why check only the left side in N-Queens?** -> Queens are placed from left to right; right columns are empty.
20. **Does 4-Queens have a solution with Queen 1 at (0, 0)?** -> No! The only solutions require Queen 1 at row 1 or 2.
21. **What is the time complexity of N-Queens?** -> $O(N!)$ in worst case.
22. **What is the difference between Backtracking and Branch & Bound?** -> Backtracking uses DFS for decision/constraint problems; Branch & Bound uses BFS/Best-First with bounds for optimization.
23. **What is Memoization?** -> Top-down caching of recursive function calls to avoid redundant computations.
24. **What is Tabulation?** -> Bottom-up iterative table filling from base cases to target solution.
25. **Is 0-1 Knapsack NP-Complete?** -> Yes, its decision version is NP-Complete and optimization version is NP-Hard.

---

### ML Top 25
26. **What is Supervised Learning?** -> Learning a mapping function from labeled input-output pairs $(X, y)$.
27. **What is the difference between Regression and Classification?** -> Regression predicts continuous numbers; classification predicts discrete categories.
28. **What is Ordinary Least Squares?** -> Method estimating linear regression coefficients by minimizing the sum of squared residuals.
29. **What is the $R^2$ score?** -> Proportion of target variance explained by features ($1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}$).
30. **Why use RMSE instead of MSE?** -> RMSE takes the square root, returning the error to original target units (\$).
31. **What is the Interquartile Range (IQR)?** -> $Q_3 - Q_1$; values outside $[Q_1 - 1.5\text{IQR}, Q_3 + 1.5\text{IQR}]$ are outliers.
32. **What is Random Forest?** -> An ensemble of decision trees trained on bootstrap samples with random feature subset splits.
33. **What is Bagging?** -> Bootstrap Aggregating: training multiple independent models and averaging their outputs to reduce variance.
34. **Why is Linear SVM better than KNN for text?** -> Text has thousands of dimensions; KNN suffers from the Curse of Dimensionality, while SVM finds an optimal maximum-margin hyperplane.
35. **What are Support Vectors?** -> The critical training points lying on margin boundaries that exclusively determine the SVM hyperplane.
36. **What is Data Leakage?** -> When information from outside the training dataset (like test statistics) is inadvertently used during training.
37. **Why fit scaler only on training data?** -> To avoid data leakage and simulate true unseen test performance.
38. **What does `stratify=y` do?** -> Keeps the same class distribution in both training and test sets.
39. **In medical diagnosis, why is Recall more critical than Precision?** -> A False Negative leaves a diseased patient untreated, which is life-threatening.
40. **Why replace medical zeros with median?** -> Physiological measurements (glucose, BP) cannot be zero in living patients; zeros are missing data.
41. **What is the Curse of Dimensionality?** -> As dimensions grow, feature space volume explodes and points become equidistant, degrading distance-based models.
42. **What is a Multilayer Perceptron?** -> A feedforward neural network with input, hidden, and output layers and non-linear activations.
43. **Why do we need non-linear activation functions?** -> Without non-linearity, stacking layers collapses into a simple linear regression model.
44. **Why is ReLU preferred over Sigmoid?** -> ReLU ($\max(0, z)$) does not saturate for positive values, avoiding the vanishing gradient problem.
45. **What is Backpropagation?** -> An algorithm calculating loss gradients with respect to weights using the calculus chain rule.
46. **What does `early_stopping=True` do?** -> Stops training when validation performance ceases to improve, preventing overfitting.
47. **What is Unsupervised Learning?** -> Discovering natural patterns or groupings from unlabeled data without target labels.
48. **What is the Elbow Method?** -> Plotting cluster count $K$ vs Inertia (WCSS) to find the inflection point for optimal $K$.
49. **What does `model.inertia_` represent?** -> Within-Cluster Sum of Squares (WCSS): sum of squared distances of points to their centroids.
50. **What is the time complexity of K-Means vs Hierarchical?** -> K-Means is linear $O(n \cdot k \cdot t)$; Hierarchical is quadratic/cubic $O(n^2 \log n)$ or $O(n^3)$.
