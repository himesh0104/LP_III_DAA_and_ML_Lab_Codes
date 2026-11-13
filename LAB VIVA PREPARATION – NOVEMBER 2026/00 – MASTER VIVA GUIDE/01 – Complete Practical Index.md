# MASTER VIVA GUIDE: COMPLETE PRACTICAL INDEX
### Savitribai Phule Pune University (SPPU) – Laboratory Practice III (410246)
**Companion Courses:** Design and Analysis of Algorithms (410241) & Machine Learning (410242)

---

## Group A: Design and Analysis of Algorithms (DAA)

| Practical No. | Practical Title | Paradigm | Primary Data Structure | Time Complexity | Space Complexity |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **DAA 1** | Fibonacci Numbers Calculation (Recursive vs. Non-Recursive) | Recursion vs. Iteration | Call Stack vs. Scalar Variables | Rec: $O(2^n)$<br>Iter: $O(n)$ | Rec: $O(n)$<br>Iter: $O(1)$ |
| **DAA 2** | Huffman Encoding | Greedy Method | Min-Heap / Priority Queue | $O(n \log n)$ | $O(n)$ |
| **DAA 3** | Fractional Knapsack Problem | Greedy Method | Array / Tuples (Value Density Sort) | $O(n \log n)$ | $O(1)$ |
| **DAA 4** | 0-1 Knapsack Problem | Dynamic Programming | 2D Array / 1D DP Array | $O(n \cdot W)$ | $O(n \cdot W)$ or $O(W)$ |
| **DAA 5** | N-Queens Problem with First Queen Placed | Backtracking | 2D Chessboard Matrix | $O(N!)$ | $O(N^2)$ |

---

## Group B: Machine Learning (ML)

| Practical No. | Practical Title | Task Type | Algorithms Used | Key Dataset | Primary Evaluation Metrics |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **ML 1** | Uber Ride Price Prediction | Supervised Regression | Linear Regression vs. Random Forest Regressor | `uber.csv` (200k records) | $R^2$ Score, RMSE, MAE |
| **ML 2** | Email Spam Detection | Supervised Binary Classification | K-Nearest Neighbors (KNN) vs. Support Vector Machine (Linear SVM) | `emails.csv` (5,172 emails, 3,000 words) | Accuracy, Confusion Matrix, Precision, Recall, F1-Score |
| **ML 3** | Bank Customer Churn Prediction | Supervised Binary Classification | Artificial Neural Networks / Multilayer Perceptron (`MLPClassifier`) | `Churn_Modelling.csv` (10k records) | Accuracy, Confusion Matrix, Classification Report |
| **ML 4** | Diabetes Diagnosis Classification | Supervised Binary Classification | K-Nearest Neighbors (`KNeighborsClassifier`) with Median Imputation | `diabetes.csv` (768 patient records) | Accuracy, Error Rate, Precision, Recall |
| **ML 5** | Customer Sales Segmentation | Unsupervised Clustering | K-Means Clustering vs. Agglomerative Hierarchical Clustering | `sales_data_sample.csv` (2,823 transactions) | Elbow Method (WCSS / Inertia), Dendrogram |

---

## Additional Curricular Deliverables Identified in Repository
1. **DAA Mini Project:** Multi-threaded Matrix Multiplication vs. Sequential Benchmarking (Authored by Himesh Kolcharlwar, Div B, Roll B-19).
2. **ML Mini Project:** Titanic Passenger Survival Prediction Pipeline using Scikit-Learn.
3. **Blockchain Technology (BT 1A):** MetaMask Wallet setup, Sepolia test network, and Ethereum gas/transaction fee study.
