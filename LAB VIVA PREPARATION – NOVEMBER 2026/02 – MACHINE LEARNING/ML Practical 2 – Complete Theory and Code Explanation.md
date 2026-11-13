# ML Practical 2: Email Spam Binary Classification (KNN & SVM)

## A. Practical Overview
- **Practical Number:** Group B - Practical 2 (Assignment No. 7)
- **Title:** Email Spam Detection using K-Nearest Neighbors and Support Vector Machine
- **Aim:** Classify emails into spam (1) or non-spam (0) using `emails.csv`. Compare the performance of K-Nearest Neighbors (KNN) and Support Vector Machine (SVM) using accuracy, confusion matrix, and classification report.
- **Objective:**
  1. Understand binary text classification on high-dimensional word frequency data.
  2. Implement feature scaling using `StandardScaler` to prevent feature dominance.
  3. Understand instance-based learning (KNN) vs. maximum-margin hyperplane optimization (SVM).
  4. Evaluate models using Confusion Matrix, Precision, Recall, and F1-Score.
- **What Problem Does This Solve?**
  Automating the classification of incoming email traffic into legitimate communication (Ham) versus unsolicited spam. It tackles high-dimensional sparse feature spaces (3,000 dictionary words).
- **Why Are These Algorithms Required?**
  - **KNN:** Non-parametric, distance-based algorithm representing lazy learners.
  - **SVM (Linear Kernel):** Specifically engineered for high-dimensional text classification; finds the maximum-margin hyperplane separating classes.
- **Real-World Applications:**
  - Email spam filtering (Gmail, Outlook).
  - Sentiment analysis on customer reviews and tweets.
  - Phishing detection and malware URL classification.

---

## B. Theoretical Foundation
### 1. High-Dimensional Text Representation (Bag of Words)
The dataset `emails.csv` has 5,172 emails and 3,002 columns.
- `Email No.`: Identifier string (e.g. `Email 1`).
- 3,000 word columns: Represent frequency counts of specific English vocabulary words in each email.
- `Prediction`: Binary target (0 = Not Spam / Ham, 1 = Spam).

### 2. K-Nearest Neighbors (KNN)
- **Concept:** "Birds of a feather flock together." A test email is classified by finding its $k$ closest neighbors in Euclidean feature space:
  $$d(x, y) = \sqrt{\sum_{i=1}^p (x_i - y_i)^2}$$
- **Voting:** Class label is assigned by the majority vote among the $k$ nearest neighbors.
- **Lazy Learner:** KNN does zero computation during training (`fit` merely stores vectors). All computations happen during prediction.
- **Sensitivity:** Highly sensitive to irrelevant features and scale; requires feature normalization!

### 3. Support Vector Machine (Linear SVM)
- **Concept:** Finds the optimal separating hyperplane:
  $$w^T x + b = 0$$
- **Maximum Margin Principle:** Maximizes the geometric margin $rac{2}{||w||}$ between the two classes.
- **Support Vectors:** The critical data points lying closest to the decision boundary. Only these points determine the hyperplane's orientation; all other points can be removed without altering the decision surface!
- **Convex Optimization:**
  $$\min_{w, b} rac{1}{2} ||w||^2 \quad 	ext{subject to } y_i (w^T x_i + b) \ge 1$$
- **Linear Kernel:** Highly effective for text because text datasets have huge dimensionality ($p = 3000$) where data is almost always linearly separable.

### 4. Classification Evaluation Metrics
1. **Confusion Matrix:**
   $$egin{pmatrix} 	ext{TN} & 	ext{FP} \ 	ext{FN} & 	ext{TP} \end{pmatrix}$$
   - **True Positive (TP):** Actual Spam, Predicted Spam.
   - **True Negative (TN):** Actual Ham, Predicted Ham.
   - **False Positive (FP - Type I Error):** Actual Ham, Predicted Spam (Catastrophic: important email lost in spam folder!).
   - **False Negative (FN - Type II Error):** Actual Spam, Predicted Ham (Inconvenient spam in inbox).
2. **Accuracy:** $rac{	ext{TP} + 	ext{TN}}{	ext{TP} + 	ext{TN} + 	ext{FP} + 	ext{FN}}$.
3. **Precision:** $rac{	ext{TP}}{	ext{TP} + 	ext{FP}}$ (Out of all emails flagged as spam, what fraction is truly spam?).
4. **Recall (Sensitivity):** $rac{	ext{TP}}{	ext{TP} + 	ext{FN}}$ (Out of all actual spam emails, what fraction did we catch?).
5. **F1-Score:** Harmonic mean: $2 	imes rac{	ext{Precision} 	imes 	ext{Recall}}{	ext{Precision} + 	ext{Recall}}$.

---

## C. Complete Code Explanation

### Prescribed Practical Code:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Read dataset
df = pd.read_csv("emails.csv")
df = df.drop_duplicates()

# 2. Separate features and target
target = "Prediction"
X = df.drop(columns=[target, "Email No."], errors="ignore")
y = df[target]

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Normalize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Train and compare classifiers
models = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "SVM": SVC(kernel="linear")
}

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print("\n", name)
    print("Accuracy:", accuracy_score(y_test, pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
    print("Classification Report:\n",
          classification_report(y_test, pred, zero_division=0))
```

### Line-by-Line Breakdown:
1. `import pandas as pd`: Imports Pandas for tabular dataset manipulation.
2. `from sklearn.model_selection import train_test_split`: Function for partitioning data.
3. `from sklearn.preprocessing import StandardScaler`: Z-score scaler ($z = rac{x - \mu}{\sigma}$).
4. `from sklearn.neighbors import KNeighborsClassifier`: KNN algorithm implementation.
5. `from sklearn.svm import SVC`: Support Vector Classifier module.
6. `from sklearn.metrics ...`: Imports classification assessment functions.
7. `df = pd.read_csv("emails.csv")`: Loads the 5,172 email records with 3,000 word columns.
8. `X = df.drop(columns=[target, "Email No."], errors="ignore")`: Isolates the 3,000 word frequency features, dropping string labels and target.
9. `y = df[target]`: Target vector containing 0s (ham) and 1s (spam).
10. `train_test_split(..., stratify=y)`:
    - **Crucial Viva Concept: Stratification!** `stratify=y` guarantees that the proportion of spam to non-spam in `y_train` and `y_test` exactly mirrors the original dataset distribution.
11. `scaler = StandardScaler()`:
12. `X_train = scaler.fit_transform(X_train)`: Computes mean $\mu$ and standard deviation $\sigma$ exclusively on training data and scales it.
13. `X_test = scaler.transform(X_test)`:
    - **Data Leakage Prevention:** Uses the training set's $\mu$ and $\sigma$ to transform the test set. NEVER call `fit_transform` on test data!
14. `models = {"KNN": KNeighborsClassifier(n_neighbors=5), "SVM": SVC(kernel="linear")}`: Defines dictionary containing both classifiers. `n_neighbors=5` is standard odd number to break ties; `kernel="linear"` selects a linear decision boundary.
15. `model.fit(X_train, y_train)`: Fits each model on standardized training features.
16. `pred = model.predict(X_test)`: Predicts binary class labels for the holdout test set.
17. `accuracy_score(y_test, pred)`: Computes overall percentage of correct predictions.
18. `confusion_matrix(y_test, pred)`: Displays the $2 	imes 2$ table of TN, FP, FN, TP.
19. `classification_report(..., zero_division=0)`: Outputs precision, recall, and f1-score per class.

---

## D. Algorithm / Pseudocode

```text
Algorithm EmailSpamClassification(CSV_File):
1. Load dataset; drop duplicate records
2. Separate feature matrix X (drop 'Email No.' and 'Prediction') and label y = 'Prediction'
3. Split into (X_train, X_test, y_train, y_test) using 80/20 ratio stratified by y
4. Initialize StandardScaler S
5. X_train_scaled <- S.fit_transform(X_train)
6. X_test_scaled  <- S.transform(X_test)
7. Train KNN(n_neighbors=5) on X_train_scaled; predict on X_test_scaled
8. Train SVM(kernel='linear') on X_train_scaled; predict on X_test_scaled
9. For each model:
     Calculate Confusion Matrix
     Calculate Accuracy, Precision, Recall, F1-Score
10. Compare results (SVM achieves superior accuracy and lower test latency)
```

---

## E. High-Yield Viva Questions and Answers

**Q1: Why is Support Vector Machine (SVM) generally superior to KNN for text classification?**
*Answer:* Text data has very high dimensionality ($p = 3,000$ features). KNN suffers severely from the **Curse of Dimensionality** (Euclidean distances become uniform and equidistant). SVM finds a global maximum-margin hyperplane and is virtually immune to high dimensionality.

**Q2: What is the "Curse of Dimensionality"?**
*Answer:* As the number of feature dimensions grows, the volume of the feature space increases exponentially, making data points extremely sparse and causing distance metrics like Euclidean distance to lose discriminative power.

**Q3: What are Support Vectors in SVM?**
*Answer:* They are the data points closest to the separating hyperplane. The position and orientation of the decision boundary depend entirely on these support vectors.

**Q4: Why must we use `StandardScaler` before running KNN?**
*Answer:* KNN relies on Euclidean distance. If one feature has large counts (e.g., word count 50) and another has small counts (e.g., 0.1), the large feature will completely dominate the distance calculation without normalization.

**Q5: Why did we write `X_train = scaler.fit_transform(X_train)` but `X_test = scaler.transform(X_test)`?**
*Answer:* To prevent **Data Leakage**. The test set must simulate unseen future data; fitting the scaler on test data would leak test set distribution statistics into the training phase.

**Q6: What does `stratify=y` do in `train_test_split`?**
*Answer:* It ensures that both the training and test sets have the exact same class proportion (ratio of spam to ham) as the original dataset.

**Q7: In email spam detection, which error is more dangerous: False Positive or False Negative?**
*Answer:* **False Positive (Type I Error)** is much more dangerous because a legitimate email (job offer, banking alert) would be wrongly sent to the spam folder and missed by the user.

**Q8: Which evaluation metric measures resistance to False Positives?**
*Answer:* **Precision** ($rac{	ext{TP}}{	ext{TP} + 	ext{FP}}$). High precision guarantees very few false positives.

**Q9: Why is KNN called a "Lazy Learner"?**
*Answer:* Because it does not construct an explicit internal model or compute weights during training (`fit` just stores the training data in memory). All calculations occur during prediction time.

**Q10: What is the time complexity of KNN during training vs testing?**
*Answer:*
- Training: $O(1)$ (just storing data).
- Testing: $O(N \cdot p)$ per test sample, where $N$ is training samples and $p$ is features (making it very slow at inference time for large datasets).

**Q11: What is the purpose of selecting an odd value for $k$ (e.g. $k=5$)?**
*Answer:* In binary classification, an odd $k$ prevents tie votes between the two classes.

**Q12: What is the difference between hard-margin and soft-margin SVM?**
*Answer:* Hard-margin SVM requires strict linear separation with zero misclassifications (fails on overlapping data). Soft-margin SVM introduces slack variables $\xi_i$ and a penalty parameter $C$ to tolerate minor errors while maximizing the margin.

**Q13: What does `kernel="linear"` mean in `SVC`?**
*Answer:* It uses a linear dot-product kernel $K(x, x') = x^T x'$, meaning the decision boundary is a flat hyperplane in the original feature space.

**Q14: When would you use an RBF (Radial Basis Function) kernel instead of a linear kernel?**
*Answer:* When data is non-linearly separable and the number of features is relatively small compared to the number of samples. In high-dimensional text ($p \gg N$), linear kernel is faster and rarely underfits.

**Q15: What is the F1-Score and why is it calculated as a harmonic mean?**
*Answer:* $F_1 = 2 rac{P \cdot R}{P + R}$. The harmonic mean severely penalizes extreme imbalances between precision and recall, ensuring both must be reasonably high.

**Q16: What does `zero_division=0` in `classification_report` do?**
*Answer:* It suppresses warnings and sets metric values to 0 if a class has zero predicted instances (preventing division-by-zero crashes).

**Q17: How many classes are being predicted in this assignment?**
*Answer:* Two classes (Binary Classification): 0 for Not Spam (Ham) and 1 for Spam.

**Q18: What is the difference between parametric and non-parametric algorithms?**
*Answer:* Parametric algorithms (like Linear Regression/SVM with fixed parameters) assume a fixed functional form. Non-parametric algorithms (like KNN) make no assumptions about the data distribution and grow with data size.

**Q19: If an email contains no words from the 3,000 dictionary features, what does the feature vector look like?**
*Answer:* An all-zero vector ($[0, 0, \dots, 0]$).

**Q20: What is the prediction accuracy achieved on this dataset?**
*Answer:* Typically both achieve above 95% accuracy, with Linear SVM slightly outperforming KNN and executing predictions significantly faster.

---

## F. Practical Examination Preparation
- **Must-Remember Lines:**
  - `stratify=y` in `train_test_split`
  - Scaler rules: `fit_transform` on train, `transform` on test
  - `KNeighborsClassifier(n_neighbors=5)`
  - `SVC(kernel="linear")`
- **Execution Checklist:** If SVM takes too long on an older PC, use a smaller subset or linear solver.
- **Examiner Defense:** "Sir, Linear SVM is the gold standard for high-dimensional text classification because text is linearly separable in 3,000 dimensions and SVM is immune to the curse of dimensionality."

---

## G. Quick Revision
1. **Task:** Binary Text Classification (0: Ham, 1: Spam).
2. **Dataset:** 5,172 emails $	imes$ 3,000 word frequencies (`emails.csv`).
3. **Algorithms:** KNN ($k=5$) vs. Linear SVM ($w^Tx + b = 0$).
4. **Scaler:** `StandardScaler` (z-score normalization).
5. **Data Leakage Rule:** `fit_transform` train only, `transform` test.
6. **KNN Weakness:** Curse of dimensionality and slow testing latency.
7. **SVM Strength:** Optimal maximum-margin hyperplane, robust to high dimensions.
8. **Critical Metric:** Precision (minimizes False Positive legitimate email loss).
9. **Stratification:** Preserves class balance across train and test sets.
10. **Top Viva Question:** "Why is Linear SVM preferred over KNN for text classification and what are support vectors?"
