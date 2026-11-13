# MASTER VIVA GUIDE: TOP 25 MOST EXPECTED VIVA QUESTIONS

1. **Why does Recursive Fibonacci have $O(2^n)$ time complexity while Non-Recursive has $O(n)$?**
   - *Answer:* Naive recursion creates a binary call tree that repeatedly recalculates identical subproblems without caching them. Non-recursive computes each state bottom-up once in a simple loop.

2. **What is the Greedy Choice Property and how does Huffman Coding use it?**
   - *Answer:* The greedy choice property states that a globally optimal solution can be reached by making locally optimal choices. Huffman coding greedily merges the two lowest-frequency trees at each step using a min-heap.

3. **Why is Huffman coding called a prefix-free code?**
   - *Answer:* Because no assigned code word is a prefix of any other code word, guaranteeing unambiguous decoding from left to right without special delimiter characters.

4. **Why does the Greedy method work for Fractional Knapsack but fail for 0-1 Knapsack?**
   - *Answer:* Fractional knapsack allows continuous item division, guaranteeing 100% capacity utilization with maximum density items. In 0-1 knapsack, items cannot be broken; taking a high-ratio bulky item can leave unused space that could have yielded higher total profit with multiple smaller items.

5. **Why is 0-1 Knapsack time complexity $O(n \cdot W)$ called pseudo-polynomial?**
   - *Answer:* Because it depends on the numerical value of $W$. The true input size of $W$ is the number of bits $\log_2 W$. Expressed in terms of input bits $k$, the complexity is $O(n \cdot 2^k)$, which is exponential.

6. **In N-Queens, why does `is_safe` only check the left side?**
   - *Answer:* Because queens are placed sequentially column-by-column from column 0 to $N-1$. Columns to the right are completely empty and cannot attack.

7. **For $N = 4$, what happens when the first queen is fixed at `(0, 0)`?**
   - *Answer:* No solution exists! The only two valid 4-Queens solutions place the first queen in row 1 or row 2 of column 0. Fixing it at `(0, 0)` leads to complete backtracking exhaustion.

8. **What is the difference between Linear Regression and Random Forest Regression?**
   - *Answer:* Linear regression assumes a parametric linear relationship ($y = X\beta$). Random forest is a non-parametric ensemble of bagged decision trees that models complex non-linear interactions without functional assumptions.

9. **What does the $R^2$ score represent and can it be negative?**
   - *Answer:* $R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}$. It represents the fraction of target variance explained by the model. It can be negative if the model performs worse on test data than predicting the mean.

10. **Why is Support Vector Machine (SVM) preferred over KNN for text classification?**
    - *Answer:* Text features have thousands of dimensions (e.g. 3,000 words). KNN suffers from the Curse of Dimensionality (distances become equidistant). SVM finds a maximum-margin hyperplane and is virtually unaffected by high dimensionality.

11. **What are Support Vectors in SVM?**
    - *Answer:* They are the data points lying on the margin boundaries closest to the separating hyperplane. The decision boundary depends exclusively on these points.

12. **Why must `StandardScaler` be fitted ONLY on training data?**
    - *Answer:* To prevent **Data Leakage**. The test set simulates unseen future data. Fitting the scaler on test data leaks test distribution parameters ($\mu, \sigma$) into model training.

13. **In medical diagnosis (Diabetes), which metric is more critical: Precision or Recall?**
    - *Answer:* **Recall** is far more critical because a False Negative means a sick diabetic patient goes undiagnosed and untreated, which can be fatal. A False Positive only triggers a confirmatory re-test.

14. **Why do we replace 0 with median in columns like Glucose and Blood Pressure?**
    - *Answer:* A zero value for blood pressure or glucose in a living patient is biologically impossible. They represent missing observations. Median is used because clinical distributions are skewed by outliers.

15. **What is the role of an activation function in a neural network?**
    - *Answer:* It introduces non-linearity. Without non-linear activation functions, any multi-layer neural network collapses mathematically into a single linear regression.

16. **Why is ReLU preferred over Sigmoid in hidden layers?**
    - *Answer:* ReLU ($\max(0, z)$) has a constant derivative of 1 for positive inputs, which completely eliminates the **Vanishing Gradient Problem** and speeds up training.

17. **What is Backpropagation?**
    - *Answer:* An algorithm that computes the gradient of the loss function with respect to every weight in the network using the calculus chain rule, propagating errors backwards from output to input.

18. **What is the Elbow Method in K-Means?**
    - *Answer:* A plot of cluster count $K$ versus Within-Cluster Sum of Squares (Inertia). The inflection point (where inertia decrease sharply levels off) represents the optimal number of clusters.

19. **What is `k-means++` initialization?**
    - *Answer:* A method of initializing cluster centroids by spreading them far apart with probability proportional to squared distance, preventing poor local minima.

20. **What is the time complexity of K-Means vs Hierarchical Agglomerative Clustering?**
    - *Answer:* K-Means is linear $O(n \cdot k \cdot t)$; Hierarchical clustering is $O(n^2 \log n)$ or $O(n^3)$, making it too slow for very large datasets.

21. **What is the Dummy Variable Trap?**
    - *Answer:* Perfect multicollinearity caused when all one-hot encoded categories are included. It is resolved by dropping one column (`drop_first=True`).

22. **What does `stratify=y` do in `train_test_split`?**
    - *Answer:* It forces the train and test subsets to maintain the exact same class proportion as the original dataset.

23. **What is the difference between Overfitting and Underfitting?**
    - *Answer:* Overfitting = High variance, low bias (model memorizes training noise). Underfitting = High bias, low variance (model is too simple to capture patterns).

24. **What is the difference between Backtracking and Branch & Bound?**
    - *Answer:* Backtracking uses Depth-First Search for decision/constraint satisfaction problems. Branch and Bound uses Breadth-First/Best-First search with priority queues for optimization problems.

25. **What is the formula for the Interquartile Range (IQR)?**
    - *Answer:* $\text{IQR} = Q_3 - Q_1$. Outliers lie outside $[Q_1 - 1.5 \times \text{IQR}, \; Q_3 + 1.5 \times \text{IQR}]$.
