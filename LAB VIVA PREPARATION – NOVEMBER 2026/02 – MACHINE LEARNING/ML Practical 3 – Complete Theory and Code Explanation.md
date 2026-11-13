# ML Practical 3: Bank Customer Churn Prediction (Neural Networks / MLPClassifier)

## A. Practical Overview
- **Practical Number:** Group B - Practical 3 (Assignment No. 8)
- **Title:** Bank Customer Churn Prediction using Artificial Neural Networks
- **Aim:** Given a bank customer, build a neural network-based classifier (`MLPClassifier`) that can determine whether they will leave (churn) or not in the next 6 months using `Churn_Modelling.csv`. Distinguish features/target, normalize data, build initial model, identify points of improvement, train an improved model, and evaluate with accuracy and confusion matrix.
- **Objective:**
  1. Understand feedforward deep learning and Multilayer Perceptrons (MLP).
  2. Perform One-Hot Encoding on categorical features to prevent dummy variable trap.
  3. Master hyperparameter tuning: hidden layer architecture, activation functions, learning rates, L2 regularization (`alpha`), and early stopping.
  4. Compare baseline neural architectures against improved regularized networks.
- **What Problem Does This Solve?**
  Customer attrition (churn) directly impacts banking revenue. Acquiring a new customer costs 5x more than retaining an existing one. Predicting churn allows banks to proactively offer incentives to high-risk customers.
- **Why Is This Algorithm Required?**
  Customer financial behavior exhibits intricate non-linear patterns (e.g. balance vs. age interactions) that shallow linear models cannot easily capture. Multi-layer neural networks learn hierarchical non-linear feature representations.
- **Real-World Applications:**
  - Telecom churn prediction (identifying subscribers about to port out).
  - SaaS subscription renewals (Netflix, Spotify, AWS).
  - Credit card default and credit scoring models.

---

## B. Theoretical Foundation
### 1. Artificial Neural Network / Multilayer Perceptron (MLP)
An MLP is a supervised learning algorithm consisting of:
1. **Input Layer:** One neuron per scaled feature.
2. **Hidden Layer(s):** Intermediate neurons that compute non-linear transformations:
   $$z = W \cdot x + b$$
   $$a = f(z) = \max(0, z) \quad \text{(ReLU Activation)}$$
3. **Output Layer:** Outputs class probability using the Sigmoid (logistic) function for binary classification:
   $$\hat{y} = \sigma(z) = \frac{1}{1 + e^{-z}}$$

```
MLP Architecture:
Input Layer (Features)     Hidden Layer 1 (32)     Hidden Layer 2 (16)     Output (Churn: 0/1)
      [x1] -------------->      ( h1_1 )     ------>    ( h2_1 )     ---->     (( y_hat ))
      [x2] -------------->      ( h1_2 )     ------>    ( h2_2 )
       ..  -------------->        ...        ------>      ...
      [xp] -------------->      ( h1_32 )    ------>    ( h2_16 )
```

### 2. Forward Propagation & Backpropagation
- **Forward Propagation:** Inputs are multiplied by weight matrices, added to biases, and passed through non-linear activation functions to yield prediction $\hat{y}$.
- **Loss Function (Binary Cross-Entropy / Log Loss):**
  $$L(y, \hat{y}) = - \frac{1}{N} \sum_{i=1}^N \left[ y_i \ln \hat{y}_i + (1 - y_i) \ln (1 - \hat{y}_i) \right]$$
- **Backpropagation:** Computes partial derivatives of the loss function with respect to every weight using the Calculus **Chain Rule**:
  $$\frac{\partial L}{\partial W} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial W}$$
- **Weight Update via Adam Optimizer:**
  $$W \leftarrow W - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$
  Adam combines Adaptive Gradients (AdaGrad) and Momentum for fast, stable convergence.

### 3. Hyperparameter Improvement Strategy
1. **Deeper Architecture:** Transitioning from a single layer `(16,)` to two hidden layers `(32, 16)` allows the network to learn both low-level and abstract feature combinations.
2. **Activation Function:** `activation="relu"` solves the vanishing gradient problem common in sigmoid/tanh.
3. **L2 Regularization (`alpha=0.01`):** Adds a weight decay penalty $\frac{\alpha}{2} ||W||^2$ to the loss function to prevent weights from growing excessively large (combats overfitting).
4. **Early Stopping (`early_stopping=True`):** Automatically reserves 10% of training data as a validation set. If validation loss stops improving for several consecutive epochs, training terminates immediately, preventing overtraining.

---

## C. Complete Code Explanation

### Prescribed Practical Code:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Read dataset
df = pd.read_csv("Churn_Modelling.csv")

# 2. Remove irrelevant columns
df = df.drop(columns=["RowNumber", "CustomerId", "Surname"], errors="ignore")

# Separate features and target
X = df.drop("Exited", axis=1)
y = df["Exited"]

# Convert categorical columns into numerical columns
X = pd.get_dummies(X, columns=["Geography", "Gender"], drop_first=True)

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Normalize data (fit only on training data)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Initial neural network
model1 = MLPClassifier(
    hidden_layer_sizes=(16,),
    max_iter=300,
    random_state=42
)

model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

print("Initial Model Accuracy:", accuracy_score(y_test, pred1))

# Improved neural network
model2 = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    alpha=0.01,
    learning_rate_init=0.001,
    max_iter=500,
    early_stopping=True,
    random_state=42
)

model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)

# 5. Evaluate improved model
print("\nImproved Model Accuracy:", accuracy_score(y_test, pred2))
print("Confusion Matrix:\n", confusion_matrix(y_test, pred2))
print("Classification Report:\n",
      classification_report(y_test, pred2, zero_division=0))
```

### Line-by-Line Breakdown:
1. `from sklearn.neural_network import MLPClassifier`: Imports Scikit-Learn's multi-layer perceptron neural network classifier.
2. `df.drop(columns=["RowNumber", "CustomerId", "Surname"])`: Drops identifiers and surnames that carry no predictive power and could lead to spurious associations.
3. `X = df.drop("Exited", axis=1)`, `y = df["Exited"]`: `Exited` is the binary ground-truth target (1 = Customer Left, 0 = Customer Retained).
4. `pd.get_dummies(X, columns=["Geography", "Gender"], drop_first=True)`:
   - **One-Hot Encoding with Dummy Variable Trap Avoidance:**
   - If `Geography` has 3 values (France, Germany, Spain), `drop_first=True` creates 2 binary columns (`Geography_Germany`, `Geography_Spain`). If both are 0, France is mathematically inferred. This eliminates multicollinearity.
5. `train_test_split(..., stratify=y)`: Preserves the 80% non-churn / 20% churn ratio across train and test sets.
6. `scaler.fit_transform(X_train)`: Standardizes inputs ($z = \frac{x - \mu}{\sigma}$).
   - **Mandatory for Neural Networks:** Neural networks use gradient descent; unscaled features cause asymmetric gradients and slow or failing convergence.
7. `model1 = MLPClassifier(hidden_layer_sizes=(16,), max_iter=300)`:
   - Baseline network with a single hidden layer of 16 neurons.
8. `model2 = MLPClassifier(...)`:
   - `hidden_layer_sizes=(32, 16)`: Two hidden layers with 32 and 16 neurons respectively.
   - `activation="relu"`: Rectified Linear Unit activation function ($f(z) = \max(0, z)$).
   - `solver="adam"`: Adaptive Moment Estimation optimizer.
   - `alpha=0.01`: L2 penalty coefficient on weights.
   - `learning_rate_init=0.001`: Initial step size for gradient descent updates.
   - `max_iter=500`: Maximum number of epochs.
   - `early_stopping=True`: Halts training when validation score plateaus.
9. Evaluates and prints accuracy, confusion matrix, and full classification report.

---

## D. Algorithm / Pseudocode

```text
Algorithm BankChurnNeuralNetwork(CSV_File):
1. Load dataset into DataFrame df
2. Remove columns ['RowNumber', 'CustomerId', 'Surname']
3. Split into predictors X and label y = 'Exited'
4. Apply One-Hot Encoding to categorical columns ['Geography', 'Gender'] with drop_first=True
5. Split into (X_train, X_test, y_train, y_test) with test_size=0.20, stratified on y
6. Fit StandardScaler on X_train; transform both X_train and X_test
7. Define Baseline MLP: 1 hidden layer of 16 neurons; fit and predict
8. Define Improved MLP:
     Architecture: (32, 16) neurons
     Activation: ReLU
     Solver: Adam
     Regularization: L2 alpha = 0.01
     Early Stopping: Enabled
   Fit on X_train and predict on X_test
9. Compute and print Accuracy, Confusion Matrix, and Classification Report
```

---

## E. High-Yield Viva Questions and Answers

**Q1: What is a Multilayer Perceptron (MLP)?**
*Answer:* An MLP is a class of feedforward artificial neural network consisting of at least three layers of nodes: an input layer, one or more hidden layers, and an output layer, utilizing non-linear activation functions.

**Q2: What is the purpose of the activation function in a neural network?**
*Answer:* Activation functions introduce **non-linearity** into the network. Without non-linear activation functions, regardless of how many layers are stacked, the entire network simplifies into a single linear regression model ($W_2(W_1 x) = W'x$).

**Q3: What is the ReLU activation function and what advantage does it have over Sigmoid?**
*Answer:* $\text{ReLU}(z) = \max(0, z)$. It outputs $z$ for positive values and 0 otherwise. Unlike Sigmoid, its derivative is constant (1) for positive values, preventing the **Vanishing Gradient Problem** and accelerating convergence.

**Q4: What is the Dummy Variable Trap and how did we avoid it?**
*Answer:* It is a scenario of perfect multicollinearity where dummy variables are highly correlated (e.g., if Gender_Male=0, Gender_Female is definitely 1). We avoided it using `drop_first=True`, which drops one redundant column per category.

**Q5: Why is feature normalization (`StandardScaler`) critical for neural networks?**
*Answer:* Gradient descent updates weights proportionally to input feature values. If features have vastly different scales, the loss surface becomes stretched and eccentric, causing oscillations and slow convergence. Standardization creates a spherical loss surface.

**Q6: What is the Adam optimizer?**
*Answer:* Adam (Adaptive Moment Estimation) is an optimization algorithm that computes adaptive learning rates for each parameter by storing exponentially decaying averages of past gradients (momentum) and past squared gradients (AdaGrad/RMSProp).

**Q7: What does `hidden_layer_sizes=(32, 16)` mean?**
*Answer:* It defines a network with two hidden layers: the first hidden layer contains 32 artificial neurons, and the second contains 16 neurons.

**Q8: What is L2 Regularization and what does `alpha=0.01` do?**
*Answer:* L2 regularization adds a penalty proportional to the square of the magnitude of the weights ($\frac{\alpha}{2} ||W||^2$) to the loss function. It prevents the network from learning complex, fragile weight configurations, thereby combating overfitting.

**Q9: What does `early_stopping=True` accomplish?**
*Answer:* It splits off 10% of training data as a validation set. If the validation score fails to improve for a set number of consecutive iterations (`n_iter_no_change`), training terminates early, preventing the model from memorizing training noise.

**Q10: What is Backpropagation?**
*Answer:* Backpropagation is the algorithm used to train neural networks. It calculates the gradient of the loss function with respect to each weight by applying the Calculus **Chain Rule** backwards from the output layer to the input layer.

**Q11: What loss function does `MLPClassifier` use for binary classification?**
*Answer:* **Binary Cross-Entropy Loss** (also known as Log Loss).

**Q12: What does a single neuron calculate internally?**
*Answer:* It computes a weighted sum of its inputs plus a bias ($z = \sum w_i x_i + b$) and passes it through an activation function ($a = f(z)$).

**Q13: Why did we drop `RowNumber`, `CustomerId`, and `Surname`?**
*Answer:* Because they are non-predictive identifiers. Keeping surnames could cause the model to overfit on specific families or ethnicities without generalizable economic logic.

**Q14: What is an Epoch?**
*Answer:* One complete pass of the entire training dataset through the neural network during training.

**Q15: What is the difference between Batch Gradient Descent, Mini-batch, and Stochastic Gradient Descent?**
*Answer:*
- Batch GD updates weights once after evaluating the entire dataset.
- Stochastic GD updates weights after every single sample.
- Mini-batch GD updates weights after small batches (e.g. 32, 64 samples), balancing speed and stability.

**Q16: What is the Vanishing Gradient Problem?**
*Answer:* When using saturating activation functions like Sigmoid or Tanh, gradients in deeper layers become exponentially small during backpropagation, causing earlier layers to learn extremely slowly or stall completely.

**Q17: What was the improvement observed between Model 1 and Model 2?**
*Answer:* Model 2 improved generalization accuracy (from ~86.0% to ~86.2%+) and achieved better precision/recall balance on churners by leveraging two hidden layers, ReLU activation, L2 regularization, and early stopping.

**Q18: What is the output layer activation for binary classification in MLPClassifier?**
*Answer:* The Logistic **Sigmoid** function, which outputs a probability value bounded in $[0, 1]$.

**Q19: If an examiner asks: "Is customer churn an imbalanced dataset?", what is your response?**
*Answer:* Yes. In this dataset, approximately 80% of customers stay (0) and only 20% churn (1). Because of this imbalance, evaluating precision, recall, and confusion matrix is far more important than looking at accuracy alone.

**Q20: What is the difference between a Perceptron and a Multi-Layer Perceptron?**
*Answer:* A single perceptron has no hidden layers and can only classify linearly separable patterns (fails on XOR). An MLP has one or more hidden layers with non-linear activations and can approximate any continuous non-linear function (Universal Approximation Theorem).

---

## F. Practical Examination Preparation
- **Must-Remember Lines:**
  - One-hot encoding: `X = pd.get_dummies(X, columns=["Geography", "Gender"], drop_first=True)`
  - Scaler: `scaler = StandardScaler(); X_train = scaler.fit_transform(X_train); X_test = scaler.transform(X_test)`
  - Improved MLP:
    ```python
    model2 = MLPClassifier(
        hidden_layer_sizes=(32, 16), activation="relu", solver="adam",
        alpha=0.01, learning_rate_init=0.001, max_iter=500, early_stopping=True, random_state=42
    )
    ```
- **Examiner Defense:** "Sir, we improved the baseline neural network by moving to a two-tier hidden architecture (32, 16), adding ReLU non-linearity, stabilizing weights with L2 alpha=0.01, and preventing overfitting with early stopping."

---

## G. Quick Revision
1. **Task:** Binary Classification on Tabular Bank Data (`Exited` 0 or 1).
2. **Algorithm:** Multi-Layer Perceptron Classifier (`MLPClassifier`).
3. **Architecture:** Input $\rightarrow$ Hidden 1 (32) $\rightarrow$ Hidden 2 (16) $\rightarrow$ Output (Sigmoid).
4. **Activation:** ReLU ($\max(0, z)$) in hidden layers.
5. **Optimization:** Adam optimizer with backpropagation via chain rule.
6. **Loss Function:** Binary Cross-Entropy (Log Loss).
7. **Preprocessing:** Drop IDs, One-Hot Encode (`drop_first=True`), `StandardScaler`.
8. **Regularization:** L2 weight decay (`alpha=0.01`) + `early_stopping=True`.
9. **Data Imbalance:** ~80% retained, ~20% churned; necessitates confusion matrix evaluation.
10. **Top Viva Question:** "Why is ReLU preferred over Sigmoid in hidden layers, and what is the role of backpropagation?"
