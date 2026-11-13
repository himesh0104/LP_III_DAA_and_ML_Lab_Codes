# ML Practical 5: Customer Sales Clustering (K-Means & Hierarchical Clustering with Elbow Method)

## A. Practical Overview
- **Practical Number:** Group B - Practical 5 (Assignment No. 10)
- **Title:** Customer Sales Clustering using K-Means and Hierarchical Clustering
- **Aim:** Implement K-Means clustering and hierarchical (agglomerative) clustering on `sales_data_sample.csv`. Determine the optimal number of clusters using the Elbow Method (WCSS/Inertia).
- **Objective:**
  1. Understand Unsupervised Machine Learning principles.
  2. Implement the Elbow Method by evaluating Within-Cluster Sum of Squares (WCSS / Inertia).
  3. Partition data into cohesive customer segments using K-Means.
  4. Compare centroid-based partitioning (K-Means) with bottom-up hierarchical agglomerative clustering.
- **What Problem Does This Solve?**
  Customer segmentation without predefined labels. It groups purchasing records by order volume, unit price, and total monetary sales to discover natural customer cohorts (e.g. bulk wholesale buyers vs. retail consumers).
- **Why Are These Algorithms Required?**
  - **K-Means:** Highly scalable, linear-time partitioning algorithm ($O(n \cdot k \cdot t)$) ideal for large retail transaction databases.
  - **Hierarchical Clustering:** Produces an interpretable tree structure (dendrogram) showing nested subgroup relationships without requiring $K$ to be fixed upfront.
- **Real-World Applications:**
  - Targeted marketing campaigns and customer relationship management (CRM).
  - Market basket analysis and inventory allocation.
  - Anomaly and credit card fraud detection (isolated cluster outliers).

---

## B. Theoretical Foundation
### 1. Unsupervised Learning Paradigm
Unlike supervised learning, unsupervised learning datasets contain **only input features $X$ with NO target labels $y$**. The algorithm discovers inherent mathematical structures, densities, and geometric clusters autonomously.

### 2. K-Means Clustering Algorithm
- **Objective:** Partition $N$ observations into $K$ disjoint clusters $C = \{C_1, C_2, \dots, C_K\}$, minimizing the Within-Cluster Sum of Squares (**WCSS** / **Inertia**):
  $$\text{WCSS} = \sum_{k=1}^K \sum_{x \in C_k} ||x - \mu_k||^2$$
  where $\mu_k$ is the geometric centroid (mean vector) of cluster $C_k$.

#### Iterative Execution Steps (Lloyd's Algorithm):
1. **Initialization:** Choose $K$ initial centroid positions (using `k-means++` initialization to spread centroids and prevent poor local minima).
2. **Assignment Step:** Assign each data point $x_i$ to its nearest centroid using Euclidean distance:
   $$c_i = \arg\min_k ||x_i - \mu_k||^2$$
3. **Update Step:** Recompute the centroid of each cluster as the arithmetic mean of all assigned points:
   $$\mu_k = \frac{1}{|C_k|} \sum_{x \in C_k} x$$
4. **Convergence Check:** Repeat Assignment and Update until centroids stop shifting (or maximum iterations reached).

```
Centroid Optimization Flow:
[Initial Random Centroids] -> [Assign points to closest centroid] -> [Recompute mean center]
          ^                                                                   |
          |-------------------- (Repeat until centroids stabilize) -----------|
```

### 3. The Elbow Method for Optimal $K$
- As $K$ increases from 1 to $N$, WCSS monotonically decreases (when $K = N$, WCSS = 0 because every point is its own centroid).
- **The Elbow Criterion:** Plot $K$ (from 1 to 10) on the x-axis versus Inertia (WCSS) on the y-axis.
- As $K$ increases, Inertia drops rapidly at first, then flattens out. The "elbow" point is where the rate of decrease abruptly slows down. That inflection point indicates the most cost-effective and natural number of clusters.

### 4. Hierarchical Agglomerative Clustering
- **Bottom-Up Approach:**
  1. Every data point starts in its own individual cluster ($N$ clusters).
  2. Compute pairwise distance matrix between all clusters.
  3. Merge the two closest clusters based on a **Linkage Criterion** (e.g. Ward's linkage, which minimizes within-cluster variance).
  4. Repeat until all points merge into a single root cluster.
- Can be visualized as a **Dendrogram** (tree diagram).

---

## C. Complete Code Explanation

### Prescribed Practical Code:
```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering

# 1. Read dataset
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
df = df.drop_duplicates()

# 2. Select numerical sales features
features = ["QUANTITYORDERED", "PRICEEACH", "SALES"]
X = df[features].dropna()

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Elbow method
inertia = []

for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    inertia.append(model.inertia_)

plt.plot(range(1, 11), inertia, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

# 4. Choose K by inspecting the elbow plot
k = int(input("Enter optimal number of clusters: "))

# K-Means clustering
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)

X_result = X.copy()
X_result["Cluster"] = labels

print("\nK-Means Cluster Counts:")
print(X_result["Cluster"].value_counts().sort_index())

print("\nSample Clustered Data:")
print(X_result.head(10))

# 5. Optional: Hierarchical clustering
hierarchical = AgglomerativeClustering(n_clusters=k)
X_result["Hierarchical_Cluster"] = hierarchical.fit_predict(X_scaled)

print("\nHierarchical Cluster Counts:")
print(X_result["Hierarchical_Cluster"].value_counts().sort_index())
```

### Line-by-Line Breakdown:
1. `encoding="latin1"`: The sales dataset contains special characters (currency symbols, European accents) that trigger utf-8 decoding errors. `latin1` loads the file cleanly.
2. `features = ["QUANTITYORDERED", "PRICEEACH", "SALES"]`: Selects core quantitative transactional features representing purchasing behavior.
3. `scaler = StandardScaler(); X_scaled = scaler.fit_transform(X)`: Standardizes features to zero mean and unit variance.
   - **Crucial Viva Detail:** `SALES` ranges into thousands of dollars, whereas `QUANTITYORDERED` is typically between 10 and 50. Without scaling, `SALES` would completely overpower Euclidean distance!
4. `for k in range(1, 11):`: Fits K-Means for cluster counts from 1 to 10.
5. `model = KMeans(n_clusters=k, random_state=42, n_init=10)`:
   - `n_init=10`: Runs K-Means 10 times with different random centroid initializations and selects the run with the lowest inertia.
6. `inertia.append(model.inertia_)`:
   - `model.inertia_` in scikit-learn is the exact value of WCSS ($\sum ||x - \mu||^2$).
7. `plt.plot(range(1, 11), inertia, marker="o")`: Plots the elbow curve.
8. `k = int(input("Enter optimal number of clusters: "))`: Allows dynamic assignment of optimal $K$ based on elbow inspection (e.g. $K=3$ or $K=4$).
9. `kmeans.fit_predict(X_scaled)`: Computes cluster centroids and returns the cluster index ($0 \dots K-1$) assigned to each sample.
10. `X_result["Cluster"] = labels`: Appends assigned cluster labels to original unscaled DataFrame for business interpretation.
11. `AgglomerativeClustering(n_clusters=k)`: Fits a bottom-up hierarchical clustering model using Ward's minimum variance linkage.
12. `value_counts().sort_index()`: Displays the distribution of transactions across discovered clusters.

---

## D. Algorithm / Pseudocode

```text
Algorithm CustomerSalesClustering(CSV_File):
1. Load dataset with encoding='latin1'; drop duplicates
2. Select numerical columns: ['QUANTITYORDERED', 'PRICEEACH', 'SALES']
3. Scale features using StandardScaler
4. Initialize empty list Inertia
5. For k <- 1 to 10 do:
     Fit KMeans(n_clusters=k, n_init=10) on scaled data
     Append model.inertia_ to Inertia
6. Plot k vs Inertia; find inflection elbow point K_optimal
7. Fit KMeans(n_clusters=K_optimal) -> get labels_kmeans
8. Fit AgglomerativeClustering(n_clusters=K_optimal) -> get labels_hierarchical
9. Attach cluster labels to DataFrame
10. Analyze cluster distributions and profiling
```

---

## E. High-Yield Viva Questions and Answers

**Q1: What is the primary difference between Supervised and Unsupervised Learning?**
*Answer:* Supervised learning trains on labeled data $(X, y)$ to predict a specific target. Unsupervised learning operates on unlabeled data $(X)$ to discover hidden patterns, groupings, or structures without external guidance.

**Q2: What is the Elbow Method and what is plotted on the axes?**
*Answer:* The Elbow Method is a heuristic used to determine the optimal number of clusters $K$. The x-axis plots the number of clusters $K$, and the y-axis plots **Inertia** (Within-Cluster Sum of Squares / WCSS). The point where the curve bends like an elbow represents the optimal balance between cluster compactness and complexity.

**Q3: What does `model.inertia_` represent in Scikit-Learn?**
*Answer:* It represents the Within-Cluster Sum of Squares (WCSS): the sum of squared Euclidean distances of samples to their closest cluster centroid: $\sum ||x_i - \mu_{c_i}||^2$.

**Q4: What is the time complexity of the K-Means algorithm?**
*Answer:* $O(N \cdot K \cdot I \cdot d)$, where $N$ is the number of samples, $K$ is the number of clusters, $I$ is the number of iterations until convergence, and $d$ is the number of features. It is linear in data size.

**Q5: What is the time complexity of Hierarchical Agglomerative Clustering?**
*Answer:* $O(N^2 \log N)$ or $O(N^3)$, because it must compute and update an $N \times N$ pairwise distance matrix at every merge step. This makes it impractical for very large datasets ($N > 50,000$).

**Q6: Why is `StandardScaler` mandatory for K-Means?**
*Answer:* K-Means calculates spherical Euclidean distances. Features with large numerical ranges (e.g. `SALES` up to \$10,000) will dominate the distance metric over features with small scales (e.g. `PRICEEACH` \$50), creating distorted, biased clusters.

**Q7: What does `n_init=10` mean in `KMeans`?**
*Answer:* K-Means is sensitive to initial centroid placement and can get trapped in local minima. `n_init=10` means the algorithm will run 10 separate times with different centroid seeds and return the solution with the lowest overall inertia.

**Q8: What is `k-means++` initialization?**
*Answer:* A smart initialization algorithm that chooses the first centroid uniformly at random and then selects subsequent centroids with a probability proportional to their squared distance from existing centroids. It spreads initial centroids out, dramatically speeding up convergence and avoiding poor local minima.

**Q9: What happens to Inertia when $K = N$ (number of clusters equals number of samples)?**
*Answer:* Inertia becomes **0**, because every sample is its own centroid ($||x_i - \mu_i|| = 0$).

**Q10: Can K-Means detect clusters of non-spherical or arbitrary shapes?**
*Answer:* No. K-Means assumes spherical, isotropic clusters of similar sizes. For non-spherical shapes (e.g., concentric circles, moons), density-based algorithms like **DBSCAN** or **Spectral Clustering** must be used.

**Q11: What is a Dendrogram?**
*Answer:* A tree diagram used in hierarchical clustering that illustrates the sequence of merges and the Euclidean distance at which each merge took place. Cutting the dendrogram horizontally at a chosen distance reveals the clusters.

**Q12: What is Ward's Linkage in Hierarchical Clustering?**
*Answer:* Ward's method merges the two clusters that result in the minimum increase in total within-cluster variance.

**Q13: What other linkage criteria exist besides Ward's?**
*Answer:*
- **Single Linkage:** Minimum distance between points in two clusters (prone to chaining).
- **Complete Linkage:** Maximum distance between points in two clusters.
- **Average Linkage:** Average distance between all pairs of points.

**Q14: Why did we load `sales_data_sample.csv` with `encoding="latin1"`?**
*Answer:* Because the CSV contains non-ASCII characters (European city names and currency symbols) that trigger a `UnicodeDecodeError` under default UTF-8 encoding.

**Q15: How can you evaluate clustering performance if no ground-truth labels exist?**
*Answer:* Using **Intrinsic Evaluation Metrics**, primarily the **Silhouette Coefficient** (measures how close a sample is to its own cluster compared to neighboring clusters, range $[-1, +1]$), the **Davies-Bouldin Index**, or the **Calinski-Harabasz Index**.

**Q16: What does a Silhouette Score close to +1 indicate?**
*Answer:* It indicates that data points are very well matched to their own cluster and poorly matched to neighboring clusters (ideal, dense, well-separated clusters).

**Q17: Is K-Means sensitive to outliers?**
*Answer:* Yes, highly sensitive, because centroids are computed as arithmetic means, which are pulled heavily by extreme outliers. Algorithms like **K-Medoids (PAM)** use actual data points as centers to provide robustness against outliers.

**Q18: What is the difference between Hard Clustering and Soft Clustering?**
*Answer:*
- Hard Clustering (K-Means): Each data point belongs strictly to one cluster ($0$ or $1$).
- Soft / Fuzzy Clustering (Gaussian Mixture Models / Fuzzy C-Means): Each data point has a probability distribution of belonging to each cluster.

**Q19: What business insights are extracted from clustering this sales dataset?**
*Answer:* It segments transactions into distinct tiers: e.g., Tier 1: Small recurring retail orders; Tier 2: Medium wholesale purchases; Tier 3: High-value bulk corporate enterprise contracts.

**Q20: What is the stopping criterion for K-Means?**
*Answer:* The algorithm stops when:
1. Centroids change position by less than a predefined tolerance (`tol`).
2. Cluster assignments of points do not change between iterations.
3. The maximum iteration count (`max_iter=300`) is reached.

---

## F. Practical Examination Preparation
- **Must-Remember Lines:**
  - File reading: `df = pd.read_csv("sales_data_sample.csv", encoding="latin1")`
  - Scaling: `X_scaled = StandardScaler().fit_transform(X)`
  - Elbow loop:
    ```python
    inertia = []
    for k in range(1, 11):
        model = KMeans(n_clusters=k, random_state=42, n_init=10)
        model.fit(X_scaled)
        inertia.append(model.inertia_)
    ```
  - Final fitting: `kmeans = KMeans(n_clusters=k, random_state=42, n_init=10); labels = kmeans.fit_predict(X_scaled)`
- **Examiner Defense:** "Sir, K-Means is an unsupervised partitioner minimizing WCSS, and we validated the choice of $K$ via the Elbow Method on standardized order and sales volume."

---

## G. Quick Revision
1. **Task:** Unsupervised Clustering (Customer Segmentation).
2. **Algorithms:** K-Means vs. Agglomerative Hierarchical Clustering.
3. **Features:** `QUANTITYORDERED`, `PRICEEACH`, `SALES`.
4. **Encoding:** `latin1` required for non-ASCII CSV symbols.
5. **Preprocessing:** Mandatory `StandardScaler` to equalize feature variance.
6. **Inertia / WCSS:** Within-Cluster Sum of Squares: $\sum ||x - \mu||^2$.
7. **Elbow Method:** Inflection point in $K$ vs Inertia plot determines optimal $K$.
8. **Initialization:** `k-means++` spreads initial centroids.
9. **Hierarchical Linkage:** Ward's linkage minimizes within-cluster variance.
10. **Top Viva Question:** "Explain how the Elbow Method works and why feature scaling is critical before running K-Means."
