# MASTER VIVA GUIDE: ESSENTIAL DEFINITIONS & CORE CONCEPTS

## 1. DAA Core Concepts
- **Algorithm:** A finite, well-defined, step-by-step sequence of unambiguous instructions designed to solve a specific computational problem.
- **Divide and Conquer:** A paradigm where a problem is partitioned into two or more independent subproblems of the same type, solved recursively, and their solutions combined (e.g. Merge Sort, Binary Search).
- **Greedy Method:** An algorithmic paradigm that makes the locally optimal choice at each stage with the hope of finding a global optimum. Requires the **Greedy Choice Property** and **Optimal Substructure**.
- **Dynamic Programming (DP):** An optimization method that solves complex problems by breaking them down into simpler **overlapping subproblems**, storing intermediate solutions in a table (memoization or tabulation) to avoid redundant recalculation.
- **Principle of Optimality:** An optimal policy has the property that whatever the initial state and decision are, the remaining decisions must constitute an optimal policy with regard to the state resulting from the first decision.
- **Backtracking:** A systematic depth-first search (DFS) through the solution space that abandons ("backtracks") a path as soon as a bounding function determines the candidate cannot satisfy the problem constraints.
- **Branch and Bound:** A state-space search algorithm using Breadth-First or Best-First Search with a priority queue, primarily designed for discrete combinatorial optimization problems.
- **Overlapping Subproblems:** Subproblems that are encountered repeatedly during the recursive execution of an algorithm.
- **Prefix-Free Code:** A binary coding scheme where no valid code word is a prefix of any other code word, enabling instantaneous unambiguous decoding.
- **Pseudo-Polynomial Time:** An algorithm whose running time is polynomial in the numeric value of the input, but exponential in the length of the input (number of bits, $\log W$).
- **State Space Tree:** A tree representing all possible paths/decisions from the root (initial state) to leaf nodes (solution or dead ends).
- **Bounding Function:** A heuristic test used in backtracking to prune branches of the state space tree that cannot lead to a feasible or optimal solution.
- **Time Complexity:** The mathematical measure of how the number of operations performed by an algorithm scales as a function of the input size $n$.
- **Space Complexity:** The total amount of memory (auxiliary space + input space) required by an algorithm to execute to completion.

---

## 2. Machine Learning Core Concepts
- **Machine Learning:** The field of computer science that gives computers the capability to learn and extract patterns from data without being explicitly programmed.
- **Supervised Learning:** Learning where models are trained using labeled input-output pairs $(X, y)$ to predict outputs on unseen data.
- **Unsupervised Learning:** Learning where models discover inherent structures, clusters, or distributions from unlabeled data $(X)$ with no supervision.
- **Linear Regression:** A parametric model estimating a linear relationship between independent variables $X$ and a continuous dependent variable $y$.
- **Ordinary Least Squares (OLS):** The optimization technique that minimizes the sum of squared differences between observed and predicted values.
- **Random Forest:** An ensemble meta-estimator that fits multiple decision tree classifiers/regressors on various sub-samples of the dataset and uses averaging to improve predictive accuracy and control overfitting.
- **Bagging (Bootstrap Aggregating):** Training multiple independent models on random subsets of training data sampled with replacement, then aggregating their predictions.
- **K-Nearest Neighbors (KNN):** A non-parametric, instance-based lazy learning algorithm that classifies a query point based on the majority vote of its $k$ closest neighbors in feature space.
- **Support Vector Machine (SVM):** A supervised classifier that finds the optimal hyperplane with the maximum margin separating distinct classes in multi-dimensional space.
- **Support Vectors:** The specific training data points lying on the margin boundaries that dictate the orientation of the SVM hyperplane.
- **Multilayer Perceptron (MLP):** A class of feedforward artificial neural networks consisting of input, hidden, and output layers with non-linear activation functions.
- **Activation Function:** A mathematical gate that transforms the weighted sum of inputs into an activation level, introducing non-linearity to the network.
- **ReLU (Rectified Linear Unit):** $f(z) = \max(0, z)$. Prevents vanishing gradient and enables fast computation.
- **Backpropagation:** The algorithm that calculates the partial derivatives of the loss function with respect to all network weights using the calculus chain rule.
- **Adam Optimizer:** An adaptive learning rate optimization algorithm combining momentum and RMSProp.
- **K-Means Clustering:** A partitioning clustering algorithm that divides $N$ observations into $K$ clusters, each represented by its centroid, minimizing within-cluster variance.
- **Elbow Method:** A technique to identify the optimal number of clusters by plotting cluster count $K$ against Within-Cluster Sum of Squares (Inertia) and finding the inflection point.
- **Hierarchical Agglomerative Clustering:** A bottom-up clustering strategy where each observation starts as its own cluster and pairs of clusters are iteratively merged up a hierarchy.
- **Confusion Matrix:** A table evaluating classification model performance showing counts of True Positives, True Negatives, False Positives, and False Negatives.
- **Precision:** $\frac{\text{TP}}{\text{TP} + \text{FP}}$. The proportion of positive identifications that were actually correct.
- **Recall (Sensitivity):** $\frac{\text{TP}}{\text{TP} + \text{FN}}$. The proportion of actual positives that were identified correctly.
- **F1-Score:** The harmonic mean of Precision and Recall ($2 \frac{P \cdot R}{P + R}$).
- **Overfitting:** When a model learns noise and fine details in the training data to the extent that it negatively impacts generalization on new data (low bias, high variance).
- **Underfitting:** When a model cannot capture the underlying trend of the data (high bias, low variance).
- **Data Leakage:** When information from outside the training dataset (such as test set statistics) is accidentally used to create the model.
- **Interquartile Range (IQR):** $Q_3 - Q_1$. A robust measure of statistical dispersion used to detect outliers.
