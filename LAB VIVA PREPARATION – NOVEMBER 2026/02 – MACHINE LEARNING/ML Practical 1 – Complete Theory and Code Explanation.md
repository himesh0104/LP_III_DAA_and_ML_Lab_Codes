# ML Practical 1: Uber Fare Price Prediction (Linear & Random Forest Regression)

## A. Practical Overview
- **Practical Number:** Group B - Practical 1 (Assignment No. 6)
- **Title:** Uber Ride Price Prediction using Linear and Random Forest Regression
- **Aim:** Predict the price of the Uber ride from a given pickup point to the agreed drop-off location using `uber.csv`. Perform preprocessing, outlier identification, correlation analysis, model building, and evaluation using $R^2$, RMSE, and MAE.
- **Objective:**
  1. Master data wrangling, handling missing values, and datetime feature extraction.
  2. Detect and remove extreme anomalies using the Interquartile Range (IQR) technique.
  3. Visualize multi-variable relationships using Pearson correlation heatmaps.
  4. Implement and benchmark parametric (Linear Regression) vs. non-parametric ensemble (Random Forest) models.
- **What Problem Does This Solve?**
  Dynamically estimating transit fare based on spatial coordinates, time of day, and seasonal trends. It teaches how to deal with noisy geospatial data, skewed financial variables, and the trade-offs between linear interpretability and non-linear ensemble accuracy.
- **Why Are These Algorithms Required?**
  - **Linear Regression:** Provides a fast, interpretable linear baseline ($y = Xeta + \epsilon$).
  - **Random Forest Regressor:** Captures non-linear geographic interactions, congestion thresholds, and time-of-day traffic dynamics without requiring manual polynomial features.
- **Real-World Applications:**
  - Dynamic pricing and surge fare estimation in ride-hailing apps (Uber, Lyft, Ola).
  - Logistics, delivery fee calculation (DoorDash, FedEx), and airline ticket pricing.

---

## B. Theoretical Foundation
### 1. Machine Learning Category: Supervised Regression
- **Supervised Learning:** The dataset contains input feature vectors $X$ paired with continuous target values $y$ (`fare_amount`).
- **Regression vs. Classification:** Regression predicts continuous numerical quantities (dollars/rupees), whereas classification predicts discrete category labels.

### 2. Mathematical Formulations
#### a) Ordinary Least Squares (Linear Regression)
Models target $\hat{y}$ as a linear combination of features:
$$\hat{y} = eta_0 + eta_1 x_1 + eta_2 x_2 + \dots + eta_p x_p = Xeta$$
Weights $eta$ are found by minimizing the Residual Sum of Squares (RSS):
$$	ext{RSS} = \sum_{i=1}^N (y_i - \hat{y}_i)^2 \implies \hat{eta} = (X^T X)^{-1} X^T y$$

#### b) Random Forest Regression (Bagging / Ensemble)
An ensemble of $B$ independent Decision Trees trained on bootstrap samples of the data:
$$\hat{y}_{	ext{RF}} = rac{1}{B} \sum_{b=1}^B T_b(x)$$
Each split considers a random subset of features ($p/3$ for regression), which decorrelates individual trees and dramatically reduces prediction variance without increasing bias.

#### c) Outlier Detection via Interquartile Range (IQR)
- $Q_1$ = 25th percentile, $Q_3$ = 75th percentile.
- $	ext{IQR} = Q_3 - Q_1$.
- Valid Range: $[Q_1 - 1.5 	imes 	ext{IQR}, \; Q_3 + 1.5 	imes 	ext{IQR}]$. Values outside are flagged as outliers.

#### d) Regression Evaluation Metrics
1. **$R^2$ Score (Coefficient of Determination):**
   $$R^2 = 1 - rac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - ar{y})^2} = 1 - rac{	ext{SS}_{	ext{res}}}{	ext{SS}_{	ext{tot}}}$$
   Measures the proportion of variance in the target explained by the model ($1.0$ is perfect; $0$ means predicting the mean).
2. **Root Mean Squared Error (RMSE):**
   $$	ext{RMSE} = \sqrt{rac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2}$$
   Measures error in the same units as the target (\$); heavily penalizes large errors due to squaring.
3. **Mean Absolute Error (MAE):**
   $$	ext{MAE} = rac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i|$$
   Linear penalty; robust to extreme outliers.

---

## C. Complete Code Explanation

### Prescribed Practical Code:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# 1. Read and preprocess dataset
df = pd.read_csv("uber.csv")
df = df.dropna()
df = df.drop_duplicates()

df = df.drop(columns=["Unnamed: 0", "key"], errors="ignore")

# Convert pickup date to numerical features
df["pickup_datetime"] = pd.to_datetime(
    df["pickup_datetime"], errors="coerce", utc=True
)
df = df.dropna(subset=["pickup_datetime"])

df["hour"] = df["pickup_datetime"].dt.hour
df["day"] = df["pickup_datetime"].dt.day
df["month"] = df["pickup_datetime"].dt.month
df = df.drop(columns=["pickup_datetime"])

# Remove invalid coordinates and fares
df = df[
    (df["fare_amount"] > 0) &
    df["pickup_longitude"].between(-180, 180) &
    df["dropoff_longitude"].between(-180, 180) &
    df["pickup_latitude"].between(-90, 90) &
    df["dropoff_latitude"].between(-90, 90)
]

# 2. Identify fare outliers using IQR
Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[
    (df["fare_amount"] < Q1 - 1.5 * IQR) |
    (df["fare_amount"] > Q3 + 1.5 * IQR)
]
print("Fare outliers:", len(outliers))

# Remove extreme fare outliers
df = df[
    df["fare_amount"].between(
        max(0, Q1 - 1.5 * IQR), Q3 + 1.5 * IQR
    )
]

# 3. Check correlation
print(df.corr(numeric_only=True)["fare_amount"].sort_values())

sns.heatmap(df.corr(numeric_only=True), cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 4. Train models
X = df.drop(columns=["fare_amount", "passenger_count"], errors="ignore")
y = df["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(
        n_estimators=100, random_state=42, n_jobs=-1
    )
}

# 5. Evaluate models
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, pred))

    print("\n", name)
    print("R2 Score:", round(r2_score(y_test, pred), 4))
    print("RMSE:", round(rmse, 4))
    print("MAE:", round(mean_absolute_error(y_test, pred), 4))
```

### Line-by-Line Breakdown:
1. `import pandas as pd`, `import numpy as np`: Core data analysis and array operations.
2. `import matplotlib.pyplot as plt`, `import seaborn as sns`: Plotting and correlation visualization.
3. `from sklearn...`: Scikit-learn imports for dataset splitting, linear model, random forest ensemble, and regression metrics.
4. `df = pd.read_csv("uber.csv")`: Loads the raw CSV into a DataFrame.
5. `df.dropna()`, `df.drop_duplicates()`: Sanitizes data by removing missing and redundant entries.
6. `df.drop(columns=["Unnamed: 0", "key"], errors="ignore")`: Removes database ID and surrogate key columns that have no predictive relationship to price.
7. `pd.to_datetime(..., utc=True)`: Converts timestamp strings into ISO datetime objects with coordinated universal time.
8. `df["hour"] = df["...dt.hour]`, `df["day"]...`, `df["month"]...`: **Feature Engineering**: Deconstructs date into separate cyclical components. Hour captures rush hour; month captures seasonality.
9. `df[...between(-180, 180)...]`: Domain constraint cleaning: Longitude must be $\in [-180, 180]$, latitude $\in [-90, 90]$, and fare must be positive ($> 0$). Drops GPS sensor glitches (e.g. coordinates at 0, 0 in Atlantic Ocean).
10. `Q1 = df["fare_amount"].quantile(0.25)` ... `IQR = Q3 - Q1`: Computes 25th, 75th percentiles and IQR spread.
11. `df[df["fare_amount"].between(...)]`: Filters out extreme fare outliers that would distort linear regression coefficients.
12. `df.corr(numeric_only=True)["fare_amount"].sort_values()`: Calculates Pearson correlation coefficients with the target fare.
13. `sns.heatmap(..., cmap="coolwarm")`: Generates visual color-coded correlation matrix.
14. `X = df.drop(...)`, `y = df["fare_amount"]`: Separates explanatory variables from the dependent target variable. Drops `passenger_count` due to near-zero correlation with fare.
15. `train_test_split(..., test_size=0.2, random_state=42)`: Holds out 20% of data for unseen testing. `random_state=42` ensures deterministic reproducibility.
16. `RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)`: Initializes 100 decision trees; `n_jobs=-1` utilizes all available CPU cores for parallel training.
17. `rmse = np.sqrt(mean_squared_error(y_test, pred))`: Computes root mean squared error.
18. Prints $R^2$, RMSE, and MAE for direct model comparison.

---

## D. Algorithm / Pseudocode

```text
Algorithm UberFarePipeline(CSV_File):
1. Load dataset into DataFrame D
2. Drop rows with nulls or duplicate rows
3. Drop non-predictive identifiers ('Unnamed: 0', 'key')
4. Parse 'pickup_datetime' -> extract 'hour', 'day', 'month'; drop original datetime column
5. Filter coordinates: Longitude in [-180, 180], Latitude in [-90, 90], Fare > 0
6. Compute Q1, Q3, IQR for 'fare_amount'
   Keep rows where Fare in [max(0, Q1 - 1.5*IQR), Q3 + 1.5*IQR]
7. Separate feature matrix X and target y = 'fare_amount'
8. Split into (X_train, X_test, y_train, y_test) with test_size = 0.20
9. For each model in [LinearRegression, RandomForestRegressor]:
     Train model on (X_train, y_train)
     Predict y_pred on X_test
     Compute R2, RMSE = sqrt(MSE(y_test, y_pred)), MAE
10. Compare performance metrics
```

---

## E. High-Yield Viva Questions and Answers

**Q1: What is the primary difference between Linear Regression and Random Forest Regression?**
*Answer:* Linear Regression is a parametric algorithm that assumes a linear relationship between features and target ($y = Xeta$). Random Forest is a non-parametric ensemble of decision trees that can model complex non-linear relationships and interactions without assumptions.

**Q2: What is the Interquartile Range (IQR) and why do we use it here?**
*Answer:* $	ext{IQR} = Q_3 - Q_1$. It defines the middle 50% spread of data. We use it to identify and remove extreme outliers (values beyond $1.5 	imes 	ext{IQR}$) which would otherwise disproportionately distort Ordinary Least Squares regression.

**Q3: Why did we extract `hour`, `day`, and `month` from `pickup_datetime`?**
*Answer:* Machine learning algorithms cannot directly process raw timestamp strings. Extracting numerical hour, day, and month allows the model to learn peak traffic hours, weekday vs weekend patterns, and monthly seasonality.

**Q4: Why did we drop the columns `Unnamed: 0` and `key`?**
*Answer:* They are arbitrary primary keys/row identifiers that carry zero physical meaning or predictive power; retaining them would cause spurious correlations or data leakage.

**Q5: What is the formula for $R^2$ and what does a value of 0.75 mean?**
*Answer:* $R^2 = 1 - rac{	ext{SS}_{	ext{res}}}{	ext{SS}_{	ext{tot}}}$. A value of 0.75 means that 75% of the total variance in ride fares is successfully explained by our model's features.

**Q6: Can $R^2$ ever be negative?**
*Answer:* Yes! If the model performs worse on test data than a simple horizontal line predicting the mean target value, $R^2$ becomes negative.

**Q7: Which metric is more sensitive to outliers: MAE or RMSE?**
*Answer:* **RMSE** is much more sensitive because individual errors are squared before averaging, meaning large prediction errors heavily penalize the score.

**Q8: Why does Random Forest perform better than Linear Regression on this dataset?**
*Answer:* Because fare calculation involves non-linear geographic factors (great-circle distances, city congestion zones) and threshold effects (night surcharges) that a simple plane cannot fit, but decision trees split effectively.

**Q9: What does `n_estimators=100` mean in RandomForestRegressor?**
*Answer:* It means the ensemble builds and averages the predictions of 100 individual decision trees.

**Q10: What does `n_jobs=-1` do?**
*Answer:* It instructs scikit-learn to utilize all available CPU cores in parallel for building decision trees, accelerating training time.

**Q11: What is the Pearson correlation coefficient range?**
*Answer:* $[-1, +1]$, where $+1$ is perfect positive linear correlation, $-1$ is perfect negative linear correlation, and $0$ indicates no linear correlation.

**Q12: Why did we filter coordinates between -90 to +90 and -180 to +180?**
*Answer:* Latitudes geographically range from $-90^\circ$ (South Pole) to $+90^\circ$ (North Pole), and Longitudes from $-180^\circ$ to $+180^\circ$. Any coordinate outside this range represents corrupted GPS sensor data.

**Q13: What is the Bagging technique used in Random Forest?**
*Answer:* Bagging (Bootstrap Aggregation) trains each tree on a random sample of the training set drawn with replacement, then averages their outputs to reduce model variance.

**Q14: What is Haversine distance and could it improve this model?**
*Answer:* The Haversine formula calculates the great-circle distance between two GPS coordinates on a sphere. Replacing raw latitude/longitude with calculated ride distance dramatically boosts model predictive accuracy.

**Q15: What is `random_state=42`?**
*Answer:* A pseudo-random seed that ensures the train-test split and random tree choices are identical every time the code is run, guaranteeing reproducible results.

**Q16: What is multicollinearity?**
*Answer:* High linear correlation between two or more independent features, which makes estimating unique coefficients unstable in Linear Regression.

**Q17: What is the difference between Mean Squared Error (MSE) and Root Mean Squared Error (RMSE)?**
*Answer:* MSE is in squared units ($\$^{2}$), which is difficult to interpret practically. RMSE takes the square root, returning the error to the original target units (\$).

**Q18: What is Overfitting and how does Random Forest combat it?**
*Answer:* Overfitting occurs when a model learns noise in training data. Random Forest combats it by averaging multiple decorrelated trees and randomly subsetting features at each split.

**Q19: Why was `passenger_count` dropped before model training?**
*Answer:* In real taxi pricing, the fare is based on distance and duration, not the number of passengers (unless excess luggage rules apply). Correlation analysis showed near-zero correlation with `fare_amount`.

**Q20: What is the baseline model in regression?**
*Answer:* A dummy regressor that simply predicts the mean of the training target ($ar{y}$) for every test sample.

---

## F. Practical Examination Preparation
- **Must-Remember Lines:**
  - Date parsing: `df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"], utc=True)`
  - Outlier IQR: `IQR = Q3 - Q1; df = df[df["fare_amount"].between(..., ...)]`
  - Split: `train_test_split(X, y, test_size=0.2, random_state=42)`
  - Metric computation: `rmse = np.sqrt(mean_squared_error(y_test, pred))`
- **What Can You Modify?** You can adjust `n_estimators=50` if execution takes too long on an old lab PC.
- **Examiner Defense:** "Sir, Random Forest outperforms Linear Regression because ride pricing exhibits non-linear relationships with time and geographic boundaries."

---

## G. Quick Revision
1. **Task:** Supervised Regression.
2. **Algorithms:** Linear Regression ($y=Xeta$) vs Random Forest (Bagged Trees).
3. **Target Feature:** `fare_amount`.
4. **IQR Outlier Bounds:** $[Q_1 - 1.5 	imes 	ext{IQR}, \; Q_3 + 1.5 	imes 	ext{IQR}]$.
5. **Geographic Constraints:** Latitude $\in [-90, 90]$, Longitude $\in [-180, 180]$.
6. **Key Metrics:** $R^2$ (variance explained), RMSE (root mean squared error), MAE.
7. **Best Model:** Random Forest Regressor (higher $R^2$, lower RMSE).
8. **Feature Engineering:** Extracted `hour`, `day`, `month` from raw datetime.
9. **`n_jobs=-1`:** Utilizes full CPU threading.
10. **Top Viva Question:** "Why do we take the square root of MSE to calculate RMSE, and what does an $R^2$ of 0.8 mean?"
