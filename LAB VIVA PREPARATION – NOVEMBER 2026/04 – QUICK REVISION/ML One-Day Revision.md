# ML ONE-DAY VIVA REVISION GUIDE

## Core Categories
- **Supervised Learning:** Labeled data $(X, y)$. Includes Regression (continuous $y$) and Classification (discrete $y$).
- **Unsupervised Learning:** Unlabeled data $(X)$. Includes Clustering (grouping) and Dimensionality Reduction (PCA).

---

## Models Used in Practicals
1. **Linear Regression:** $y = X\beta + \epsilon$. Fits hyperplane minimizing Residual Sum of Squares (RSS).
2. **Random Forest:** Ensemble of decorrelated decision trees using bagging and feature subspace sampling. High accuracy, low variance.
3. **K-Nearest Neighbors (KNN):** Lazy instance-based classifier. Classifies by majority vote of $k$ nearest Euclidean neighbors. Sensitive to scale and dimensionality.
4. **Support Vector Machine (Linear SVM):** Convex quadratic optimization finding the maximal-margin hyperplane ($w^T x + b = 0$). Driven solely by support vectors.
5. **Multilayer Perceptron (MLP):** Feedforward neural network. Uses ReLU in hidden layers, Adam optimizer, and backpropagation via calculus chain rule.
6. **K-Means Clustering:** Centroid-based partitioning minimizing Within-Cluster Sum of Squares (Inertia). Optimal $K$ found via Elbow Method.
7. **Agglomerative Clustering:** Bottom-up hierarchical merging using Ward's minimum variance linkage.

---

## Key Formulas Cheat-Sheet
- **$R^2$ Score:** $1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$
- **RMSE:** $\sqrt{\frac{1}{N} \sum (y_i - \hat{y}_i)^2}$
- **MAE:** $\frac{1}{N} \sum |y_i - \hat{y}_i|$
- **Accuracy:** $\frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}$
- **Precision:** $\frac{\text{TP}}{\text{TP} + \text{FP}}$ (Avoids False Positives)
- **Recall (Sensitivity):** $\frac{\text{TP}}{\text{TP} + \text{FN}}$ (Avoids False Negatives)
- **F1-Score:** $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$
- **StandardScaler (Z-Score):** $z = \frac{x - \mu}{\sigma}$
- **IQR (Outlier Filter):** $\text{IQR} = Q_3 - Q_1$; Bounds: $[Q_1 - 1.5 \times \text{IQR}, \; Q_3 + 1.5 \times \text{IQR}]$
- **Inertia (WCSS):** $\sum_{k=1}^K \sum_{x \in C_k} ||x - \mu_k||^2$
