# IMPORTANT CODE SNIPPETS (BLACKBOARD & ORAL VIVA CHEAT SHEET)

When an examiner says: *"Write the core logic on paper/board"*, write ONLY these essential lines!

---

## 1. DAA Practical 1: Fibonacci Numbers
```python
# Recursive Core (O(2^n) time, O(n) stack)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Iterative Core (O(n) time, O(1) space)
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

---

## 2. DAA Practical 2: Huffman Encoding
```python
import heapq

# Min-Heap Greedy Merge (O(n log n))
heap = [(freq[i], i, chars[i]) for i in range(len(chars))]
heapq.heapify(heap)
counter = len(chars)

while len(heap) > 1:
    f1, _, left = heapq.heappop(heap)
    f2, _, right = heapq.heappop(heap)
    heapq.heappush(heap, (f1 + f2, counter, (left, right)))
    counter += 1
```

---

## 3. DAA Practical 3: Fractional Knapsack
```python
# Value Density Greedy Sort (O(n log n))
items.sort(key=lambda x: x[0] / x[1], reverse=True)
total_profit = 0

for profit, weight in items:
    if capacity == 0:
        break
    if weight <= capacity:
        total_profit += profit
        capacity -= weight
    else:
        total_profit += profit * (capacity / weight)
        capacity = 0
```

---

## 4. DAA Practical 4: 0-1 Knapsack
```python
# 2D DP Table Formulation (O(n * W))
dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(W + 1):
        dp[i][w] = dp[i - 1][w]
        if weights[i - 1] <= w:
            dp[i][w] = max(dp[i][w], profits[i - 1] + dp[i - 1][w - weights[i - 1]])
```

---

## 5. DAA Practical 5: N-Queens Backtracking
```python
# Recursive Backtracking Step (O(N!))
def solve(board, col, n):
    if col >= n:
        return True
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve(board, col + 1, n):
                return True
            board[row][col] = 0  # Backtrack!
    return False
```

---

## 6. ML 1: IQR Outlier Filter & RMSE
```python
# IQR Outlier Removal
Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)
IQR = Q3 - Q1
df = df[df["fare_amount"].between(max(0, Q1 - 1.5 * IQR), Q3 + 1.5 * IQR)]

# RMSE Computation
rmse = np.sqrt(mean_squared_error(y_test, pred))
```

---

## 7. ML 2 & ML 4: StandardScaler & Stratified Split
```python
# Train-Test Split with Stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Mandatory Data Leakage Protection
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # Fit and transform TRAIN
X_test = scaler.transform(X_test)        # Only transform TEST
```

---

## 8. ML 3: One-Hot Encoding & MLPClassifier
```python
# Avoid Dummy Variable Trap
X = pd.get_dummies(X, columns=["Geography", "Gender"], drop_first=True)

# MLP Architecture
model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    alpha=0.01,
    early_stopping=True,
    random_state=42
)
```

---

## 9. ML 4: Medical Missing Value Median Imputation
```python
cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
for col in cols:
    X[col] = X[col].replace(0, float("nan")).fillna(X[col].median())
```

---

## 10. ML 5: K-Means WCSS & Elbow Method Loop
```python
inertia = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(X_scaled)
    inertia.append(km.inertia_)  # WCSS
```
