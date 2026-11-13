# MASTER VIVA GUIDE: LAST-MINUTE REVISION SHEET (VIVA CHEAT-SHEET)

### 30-Second Elevator Pitches for Every Practical

#### DAA 1: Fibonacci Numbers
- **Pitch:** "We implemented recursive ($O(2^n)$ time, $O(n)$ space) and iterative ($O(n)$ time, $O(1)$ space) Fibonacci generation. The recursive version suffers exponential blowup due to overlapping subproblems, which iteration resolves by bottom-up variable tracking."
- **Code Anchor:** `a, b = b, a + b` vs `fib(n-1) + fib(n-2)`.

#### DAA 2: Huffman Encoding
- **Pitch:** "A lossless greedy data compression algorithm that assigns variable-length prefix-free binary codes based on character frequencies using a Min-Heap in $O(n \log n)$ time. Frequent characters get shorter codes."
- **Code Anchor:** `heapq.heappush(heap, (f1+f2, counter, (left, right)))`. Tie-breaker `counter` avoids comparing nodes.

#### DAA 3: Fractional Knapsack
- **Pitch:** "A greedy optimization algorithm that sorts divisible items by profit-to-weight ratio in $O(n \log n)$ time and takes items greedily. At most one item is fractional. It guarantees global optimality because items are divisible."
- **Code Anchor:** `items.sort(key=lambda x: x[0]/x[1], reverse=True)`.

#### DAA 4: 0-1 Knapsack
- **Pitch:** "An indivisible optimization problem solved via 2D Dynamic Programming in $O(n \cdot W)$ pseudo-polynomial time. The state `dp[i][w]` chooses $\max(\text{exclude}, \text{include})$. Space can be optimized to $O(W)$ by looping backwards."
- **Code Anchor:** `dp[i][w] = max(dp[i-1][w], profits[i-1] + dp[i-1][w - weights[i-1]])`.

#### DAA 5: N-Queens (First Queen Placed at 0, 0)
- **Pitch:** "Solves constraint satisfaction on an $N \times N$ chessboard using recursive backtracking (DFS + bounding function `is_safe`) in $O(N!)$ worst-case time. For $N=4$, no solution exists with Queen at (0, 0)."
- **Code Anchor:** `board[row][col] = 1; if solve(...): return True; board[row][col] = 0`.

---

#### ML 1: Uber Fare Prediction
- **Pitch:** "Supervised regression on `uber.csv`. Cleaned GPS boundaries, removed fare outliers using IQR ($1.5 \times \text{IQR}$), extracted hour/day/month features, and compared Linear Regression vs Random Forest. Evaluated using $R^2$, RMSE, and MAE."
- **Code Anchor:** `RandomForestRegressor(n_estimators=100, n_jobs=-1)`.

#### ML 2: Email Spam Detection
- **Pitch:** "Supervised binary text classification on 5,172 emails with 3,000 word frequencies. Scaled features with `StandardScaler` and compared KNN ($k=5$) vs Linear SVM. Linear SVM performs better because high-dimensional text is linearly separable and immune to distance distortion."
- **Code Anchor:** `SVC(kernel="linear")` and `stratify=y`.

#### ML 3: Bank Customer Churn
- **Pitch:** "Predicts customer exit using an Artificial Neural Network (`MLPClassifier`). Applied One-Hot Encoding (`drop_first=True`) and `StandardScaler`. Improved baseline by using two hidden layers (32, 16), ReLU activation, Adam optimizer, L2 regularization (`alpha=0.01`), and early stopping."
- **Code Anchor:** `MLPClassifier(hidden_layer_sizes=(32, 16), activation="relu", early_stopping=True)`.

#### ML 4: Diabetes Classification
- **Pitch:** "Diagnostic classification on `diabetes.csv` using KNN ($k=5$). Replaced physiological impossible zeros in Glucose/BP/BMI with median. Recall is prioritized over Precision to eliminate life-threatening False Negatives."
- **Code Anchor:** `X[col].replace(0, np.nan).fillna(X[col].median())`.

#### ML 5: Sales Customer Clustering
- **Pitch:** "Unsupervised customer segmentation on `sales_data_sample.csv` using K-Means and Agglomerative Hierarchical Clustering. Evaluated WCSS/Inertia across $K=1 \dots 10$ using the Elbow Method to find the optimal cluster count."
- **Code Anchor:** `model.inertia_` and `AgglomerativeClustering(n_clusters=k)`.
