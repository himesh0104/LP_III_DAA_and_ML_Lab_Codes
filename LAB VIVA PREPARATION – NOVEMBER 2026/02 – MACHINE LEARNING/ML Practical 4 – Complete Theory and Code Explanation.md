# ML Practical 4: Diabetes Classification (KNN with Medical Data Preprocessing)

## A. Practical Overview
- **Practical Number:** Group B - Practical 4 (Assignment No. 9)
- **Title:** Diabetes Prediction using K-Nearest Neighbors Classifier
- **Aim:** Implement the K-Nearest Neighbors (KNN) algorithm on `diabetes.csv`. Handle invalid medical zero values, normalize features, train the model, and compute Confusion Matrix, Accuracy, Error Rate, Precision, and Recall.
- **Objective:**
  1. Understand clinical domain data cleaning (biological impossibilities).
  2. Implement median imputation for missing physiological values.
  3. Master distance-based classification using K-Nearest Neighbors.
  4. Understand medical diagnostic trade-offs: Type I error (False Positive) vs. Type II error (False Negative / missed diagnosis).
- **What Problem Does This Solve?**
  Early, non-invasive detection of diabetes based on diagnostic measurements (Glucose, Blood Pressure, Insulin, BMI, Age).
- **Why Is This Algorithm Required?**
  KNN provides an intuitive instance-based benchmark for medical diagnosis: patients with similar clinical biomarker profiles are likely to share the same diagnosis.
- **Real-World Applications:**
  - Clinical decision support systems (CDSS) for chronic disease risk scoring.
  - Patient triage in emergency rooms.
  - Preventive healthcare diagnostics.

---

## B. Theoretical Foundation
### 1. The Pima Indians Diabetes Dataset
Contains 768 patient records with 8 medical predictors:
1. `Pregnancies`: Number of times pregnant.
2. `Glucose`: Plasma glucose concentration at 2 hours in an oral glucose tolerance test.
3. `BloodPressure`: Diastolic blood pressure (mm Hg).
4. `SkinThickness`: Triceps skin fold thickness (mm).
5. `Insulin`: 2-Hour serum insulin (mu U/ml).
6. `BMI`: Body mass index ($\text{weight in kg} / (\text{height in m})^2$).
7. `DiabetesPedigreeFunction`: Genetic score based on family diabetes history.
8. `Age`: Age in years.
- Target: `Outcome` (0 = Non-diabetic, 1 = Diabetic).

### 2. Clinical Data Preprocessing: The "Zero Value" Trap
In medical data, while a pregnancy count of `0` is entirely normal, having a **Glucose of 0, Blood Pressure of 0, Skin Thickness of 0, Insulin of 0, or BMI of 0 is physiologically impossible in a living patient!**
These zeros were recorded as placeholders for **missing lab tests**.
- *Solution:* Replace `0` with `NaN` in these five columns, then impute with the **median** value of each column. (Median is chosen over mean because clinical distributions are typically skewed by extreme measurements).

### 3. K-Nearest Neighbors Algorithm
- Distance metric: Euclidean distance in standardized feature space:
  $$d(p, q) = \sqrt{\sum_{i=1}^n (p_i - q_i)^2}$$
- Select $k = 5$ closest neighbors.
- Predict class via majority voting.

### 4. Mathematical Performance Formulas
1. **Confusion Matrix:**
   $$\begin{pmatrix} \text{TN} & \text{FP} \\ \text{FN} & \text{TP} \end{pmatrix}$$
2. **Accuracy:**
   $$\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{Total Samples}}$$
3. **Error Rate (Misclassification Rate):**
   $$\text{Error Rate} = 1 - \text{Accuracy} = \frac{\text{FP} + \text{FN}}{\text{Total Samples}}$$
4. **Precision:**
   $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$
   (When the model diagnoses a patient as diabetic, how often is it correct?)
5. **Recall (Sensitivity / True Positive Rate):**
   $$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$
   (Out of all actual diabetic patients, what percentage did the model correctly diagnose?)

> **Crucial Medical Insight:** In medical screening, **Recall is the single most critical metric**. A False Positive leads to a confirmatory re-test (mild inconvenience). A **False Negative (missed diabetic patient)** leaves a diseased person untreated, leading to severe health complications or death!

---

## C. Complete Code Explanation

### Prescribed Practical Code:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix, accuracy_score,
    precision_score, recall_score
)

# 1. Read dataset
df = pd.read_csv("diabetes.csv")
df = df.drop_duplicates()

# 2. Separate features and target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Replace invalid zero values in selected medical measurements
cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
for col in cols:
    if col in X.columns:
        X[col] = X[col].replace(0, float("nan"))
        X[col] = X[col].fillna(X[col].median())

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Normalize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Train KNN model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# 6. Evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy)
print("Error Rate:", 1 - accuracy)
print("Precision:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
```

### Line-by-Line Breakdown:
1. `import pandas as pd`: Imports data wrangling library.
2. `from sklearn...`: Imports model selection, standard scaler, KNN, and diagnostic evaluation metrics.
3. `df = pd.read_csv("diabetes.csv")`: Reads the 768-row diabetes dataset.
4. `X = df.drop("Outcome", axis=1)`, `y = df["Outcome"]`: Isolates 8 medical predictor features from the binary ground truth `Outcome`.
5. `cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]`:
   - Target columns where a zero reading represents missing clinical observations.
6. `X[col] = X[col].replace(0, float("nan"))`: Converts biological zeros to IEEE NaN values.
7. `X[col] = X[col].fillna(X[col].median())`: Replaces NaN values with the median of the respective feature.
8. `train_test_split(..., test_size=0.2, stratify=y)`: 80% train, 20% test, with class ratio preservation.
9. `scaler = StandardScaler()`: Computes $z = \frac{x - \mu}{\sigma}$.
   - **Why Necessary?** Features like `Insulin` (values up to 800) and `Glucose` (up to 200) would completely overwhelm `DiabetesPedigreeFunction` (values between 0.1 and 2.5) in distance calculations without scaling.
10. `model = KNeighborsClassifier(n_neighbors=5)`:
    - Sets number of neighbors $k = 5$.
11. `model.fit(X_train, y_train)`: Memorizes training samples.
12. `y_pred = model.predict(X_test)`: Queries the 5 nearest neighbors for each test patient and assigns the majority vote class.
13. `accuracy = accuracy_score(y_test, y_pred)`: Correct predictions divided by total test set size.
14. `print("Error Rate:", 1 - accuracy)`: Misclassification rate.
15. `precision_score`, `recall_score`: Evaluates diagnostic clinical fidelity.

### Dry Run with Lab Output:
- Test Set Size: 154 patients (20% of 768).
- **Confusion Matrix Output:**
  $$\begin{pmatrix} 83 & 17 \\ 21 & 33 \end{pmatrix}$$
  - $\text{TN} = 83$ (Healthy correctly identified as healthy).
  - $\text{FP} = 17$ (Healthy incorrectly flagged as diabetic).
  - $\text{FN} = 21$ (Diabetic patients mistakenly diagnosed as healthy - Type II error!).
  - $\text{TP} = 33$ (Diabetic patients correctly diagnosed).
- **Metrics Calculation:**
  - $\text{Accuracy} = \frac{83 + 33}{154} = \frac{116}{154} \approx 75.32\%$
  - $\text{Error Rate} = 1 - 0.7532 = 24.68\%$
  - $\text{Precision} = \frac{33}{33 + 17} = \frac{33}{50} = 66.00\%$
  - $\text{Recall} = \frac{33}{33 + 21} = \frac{33}{54} \approx 61.11\%$

---

## D. Algorithm / Pseudocode

```text
Algorithm DiabetesKNNClassifier(CSV_File):
1. Load dataset; drop duplicate records
2. Extract predictor matrix X and label vector y = 'Outcome'
3. Identify invalid zeros in ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
4. For each invalid column:
     Replace 0 with NaN
     Replace NaN with median(column)
5. Partition into train (80%) and test (20%) sets stratified on y
6. Fit StandardScaler on X_train; transform X_train and X_test
7. Initialize KNN with k = 5
8. Fit KNN model on X_train_scaled
9. Generate predictions y_pred on X_test_scaled
10. Calculate:
      CM = Confusion_Matrix(y_test, y_pred)
      Accuracy = (TP + TN) / Total
      Error_Rate = 1 - Accuracy
      Precision = TP / (TP + FP)
      Recall = TP / (TP + FN)
11. Output performance metrics
```

---

## E. High-Yield Viva Questions and Answers

**Q1: Why is it necessary to replace zeros with median in columns like Glucose and BMI?**
*Answer:* Because in a living human being, glucose, blood pressure, insulin, skin thickness, and BMI cannot be zero. These zero values represent missing lab tests. Replacing them with the median restores realistic physiological distributions without being skewed by outliers.

**Q2: Why did we choose Median imputation instead of Mean imputation?**
*Answer:* Clinical distributions (such as insulin levels) are heavily right-skewed with extreme high outliers. The mean is strongly pulled by outliers, whereas the median is a robust measure of central tendency.

**Q3: What is the Error Rate formula and what is its relationship to Accuracy?**
*Answer:* $\text{Error Rate} = 1 - \text{Accuracy} = \frac{\text{FP} + \text{FN}}{\text{Total Samples}}$. It represents the proportion of misclassified samples.

**Q4: In this medical diagnostic problem, is Precision or Recall more important? Why?**
*Answer:* **Recall** is much more important. A False Negative means a diabetic patient goes undiagnosed and untreated, which can lead to life-threatening complications. A False Positive simply results in a secondary confirmatory blood test.

**Q5: What is the impact of choosing $k$ too small (e.g., $k=1$)?**
*Answer:* When $k=1$, the model becomes highly sensitive to noise and outliers in the training data, leading to **high variance and overfitting** (decision boundary is extremely jagged).

**Q6: What is the impact of choosing $k$ too large (e.g., $k=100$)?**
*Answer:* When $k$ is very large, the model smooths out decision boundaries excessively and simply predicts the majority class, leading to **high bias and underfitting**.

**Q7: How do you choose the optimal value of $k$?**
*Answer:* Using **Cross-Validation** (e.g. 5-fold or 10-fold CV) or plotting the error rate against various values of $k$ ($k = 1, 3, 5, \dots$) and picking the $k$ that minimizes validation error. A common heuristic is $k \approx \sqrt{N}$.

**Q8: Why must $k$ be an odd number in binary classification?**
*Answer:* To avoid tie votes when determining the majority class among the neighbors.

**Q9: What happens if you run KNN on this dataset without `StandardScaler`?**
*Answer:* Features with large numerical ranges (e.g., `Insulin` with values up to 800) will dominate the Euclidean distance calculation, rendering features with small ranges (e.g., `DiabetesPedigreeFunction` $\in [0.1, 2.5]$) virtually useless.

**Q10: What distance metric does Scikit-Learn's `KNeighborsClassifier` use by default?**
*Answer:* **Minkowski distance** with parameter $p=2$, which is mathematically equivalent to standard **Euclidean distance**.

**Q11: What is Manhattan distance and when is it preferred over Euclidean distance?**
*Answer:* Manhattan distance ($L_1$ norm) is $d(x, y) = \sum |x_i - y_i|$. It is preferred in grid-like feature spaces and is less sensitive to extreme outliers than Euclidean distance ($L_2$ norm).

**Q12: In the output confusion matrix `[[83, 17], [21, 33]]`, how many patients were diabetic in the test set?**
*Answer:* Actual diabetic patients = $\text{FN} + \text{TP} = 21 + 33 = 54$ patients.

**Q13: How many patients did the model predict as diabetic?**
*Answer:* Predicted diabetic = $\text{FP} + \text{TP} = 17 + 33 = 50$ patients.

**Q14: What is the difference between Sensitivity and Specificity?**
*Answer:*
- Sensitivity (Recall) = True Positive Rate = $\frac{\text{TP}}{\text{TP} + \text{FN}}$.
- Specificity = True Negative Rate = $\frac{\text{TN}}{\text{TN} + \text{FP}}$ (ability to correctly identify non-diabetic individuals).

**Q15: What is the ROC curve and AUC?**
*Answer:* The Receiver Operating Characteristic (ROC) curve plots True Positive Rate (Recall) vs False Positive Rate ($1 - \text{Specificity}$) across all classification thresholds. AUC (Area Under Curve) measures overall diagnostic discrimination capability ($1.0$ is perfect; $0.5$ is random guessing).

**Q16: Is KNN sensitive to imbalanced datasets?**
*Answer:* Yes. If the majority class dominates the training data, test points are more likely to have majority class samples among their nearest neighbors, biasing predictions towards the majority class.

**Q17: Why did we drop duplicate rows with `df.drop_duplicates()`?**
*Answer:* Duplicate records in clinical datasets are typically data entry errors that can cause artificial data leakage if split between training and test sets.

**Q18: What is the time complexity to predict one test point using brute-force KNN?**
*Answer:* $O(N \cdot d)$, where $N$ is the number of training points and $d$ is the number of features.

**Q19: Can KNN handle missing data natively during distance computation?**
*Answer:* Standard KNN cannot compute Euclidean distance with `NaN` values, which is why explicit imputation (median fill) is mandatory before fitting.

**Q20: What is weighted KNN (`weights='distance'`)?**
*Answer:* An enhancement where closer neighbors have a greater vote weight (proportional to $\frac{1}{d}$) than distant neighbors, reducing the sensitivity to the exact value of $k$.

---

## F. Practical Examination Preparation
- **Must-Remember Lines:**
  - Zero replacement:
    ```python
    cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    for col in cols:
        X[col] = X[col].replace(0, float("nan")).fillna(X[col].median())
    ```
  - Standard scaling: `X_train = scaler.fit_transform(X_train); X_test = scaler.transform(X_test)`
  - KNN model: `model = KNeighborsClassifier(n_neighbors=5); model.fit(X_train, y_train)`
  - Metrics: `accuracy = accuracy_score(y_test, y_pred); error_rate = 1 - accuracy`
- **Examiner Defense:** "Sir, the critical step in this practical is recognizing that physiological zeros in blood pressure and glucose are missing data that require domain-appropriate median imputation."

---

## G. Quick Revision
1. **Task:** Binary Classification on Medical Data (`Outcome`: 0 or 1).
2. **Algorithm:** K-Nearest Neighbors ($k=5$, Euclidean distance).
3. **Medical Zero Trap:** 0 in Glucose/BP/BMI = missing data $\rightarrow$ impute with median.
4. **Distance Sensitivity:** Requires `StandardScaler` to equalize feature scales.
5. **Key Formulas:**
   - $\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{Total}}$
   - $\text{Error Rate} = 1 - \text{Accuracy}$
   - $\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$
   - $\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$
6. **Clinical Priority:** Recall is prioritized to minimize life-threatening False Negatives.
7. **Small $k$:** Overfitting (High variance).
8. **Large $k$:** Underfitting (High bias).
9. **Tie-Breaking:** Odd $k=5$ prevents 50/50 vote deadlocks.
10. **Top Viva Question:** "Why are zeros replaced in clinical datasets and why is Recall more critical than Precision in medical diagnosis?"
