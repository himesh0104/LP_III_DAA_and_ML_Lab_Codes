# -*- coding: utf-8 -*-
"""
ALL ML PRACTICAL PROGRAMS (1 TO 5)
Savitribai Phule Pune University (SPPU) - LP-III
Authored for Viva & Practical Exam Mastery
"""

import os
import pandas as pd
import numpy as np

# Set working directory to dataset directory if needed
base_dir = r"c:\Users\himes\Desktop\Mini-Projects"

# =============================================================
# ML PRACTICAL 1: UBER RIDE PRICE PREDICTION (REGRESSION)
# =============================================================
def run_ml1():
    print("\n--- ML PRACTICAL 1: UBER FARE PREDICTION ---")
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

    csv_path = os.path.join(base_dir, "uber.csv")
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    df = pd.read_csv(csv_path).dropna().drop_duplicates()
    df = df.drop(columns=["Unnamed: 0", "key"], errors="ignore")

    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"], errors="coerce", utc=True)
    df = df.dropna(subset=["pickup_datetime"])
    df["hour"] = df["pickup_datetime"].dt.hour
    df["day"] = df["pickup_datetime"].dt.day
    df["month"] = df["pickup_datetime"].dt.month
    df = df.drop(columns=["pickup_datetime"])

    df = df[
        (df["fare_amount"] > 0) &
        df["pickup_longitude"].between(-180, 180) &
        df["dropoff_longitude"].between(-180, 180) &
        df["pickup_latitude"].between(-90, 90) &
        df["dropoff_latitude"].between(-90, 90)
    ]

    # IQR outlier filtering
    Q1 = df["fare_amount"].quantile(0.25)
    Q3 = df["fare_amount"].quantile(0.75)
    IQR = Q3 - Q1
    df = df[df["fare_amount"].between(max(0, Q1 - 1.5 * IQR), Q3 + 1.5 * IQR)]

    X = df.drop(columns=["fare_amount", "passenger_count"], errors="ignore")
    y = df["fare_amount"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=50, random_state=42, n_jobs=-1)
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, pred))
        print(f"\n{name} Results:")
        print(f"  R2 Score : {r2_score(y_test, pred):.4f}")
        print(f"  RMSE     : {rmse:.4f}")
        print(f"  MAE      : {mean_absolute_error(y_test, pred):.4f}")

# =============================================================
# ML PRACTICAL 2: EMAIL SPAM DETECTION (KNN & SVM)
# =============================================================
def run_ml2():
    print("\n--- ML PRACTICAL 2: EMAIL SPAM CLASSIFICATION ---")
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

    csv_path = os.path.join(base_dir, "emails.csv")
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    df = pd.read_csv(csv_path).drop_duplicates()
    X = df.drop(columns=["Prediction", "Email No."], errors="ignore")
    y = df["Prediction"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    models = {
        "KNN (k=5)": KNeighborsClassifier(n_neighbors=5),
        "Linear SVM": SVC(kernel="linear")
    }

    for name, model in models.items():
        print(f"\nTraining {name}...")
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        print(f"{name} Accuracy: {accuracy_score(y_test, pred):.4f}")
        print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
        print("Classification Report:\n", classification_report(y_test, pred, zero_division=0))

# =============================================================
# ML PRACTICAL 3: BANK CHURN PREDICTION (NEURAL NETWORK)
# =============================================================
def run_ml3():
    print("\n--- ML PRACTICAL 3: BANK CUSTOMER CHURN (ANN) ---")
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.neural_network import MLPClassifier
    from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

    csv_path = os.path.join(base_dir, "Churn_Modelling.csv")
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    df = pd.read_csv(csv_path).drop(columns=["RowNumber", "CustomerId", "Surname"], errors="ignore")
    X = df.drop("Exited", axis=1)
    y = df["Exited"]
    X = pd.get_dummies(X, columns=["Geography", "Gender"], drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Training Improved MLPClassifier (32, 16 neurons)...")
    model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        solver="adam",
        alpha=0.01,
        learning_rate_init=0.001,
        max_iter=500,
        early_stopping=True,
        random_state=42
    )
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(f"\nModel Accuracy: {accuracy_score(y_test, pred):.4f}")
    print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
    print("Classification Report:\n", classification_report(y_test, pred, zero_division=0))

# =============================================================
# ML PRACTICAL 4: DIABETES DIAGNOSIS (KNN)
# =============================================================
def run_ml4():
    print("\n--- ML PRACTICAL 4: DIABETES DIAGNOSIS (KNN) ---")
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

    csv_path = os.path.join(base_dir, "diabetes.csv")
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    df = pd.read_csv(csv_path).drop_duplicates()
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    for col in cols:
        if col in X.columns:
            X[col] = X[col].replace(0, float("nan")).fillna(X[col].median())

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)
    print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
    print(f"Accuracy   : {acc:.4f}")
    print(f"Error Rate : {1 - acc:.4f}")
    print(f"Precision  : {precision_score(y_test, pred, zero_division=0):.4f}")
    print(f"Recall     : {recall_score(y_test, pred, zero_division=0):.4f}")

# =============================================================
# ML PRACTICAL 5: CUSTOMER SALES CLUSTERING (K-MEANS)
# =============================================================
def run_ml5():
    print("\n--- ML PRACTICAL 5: SALES CUSTOMER CLUSTERING ---")
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans, AgglomerativeClustering

    csv_path = os.path.join(base_dir, "sales_data_sample.csv")
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    df = pd.read_csv(csv_path, encoding="latin1").drop_duplicates()
    X = df[["QUANTITYORDERED", "PRICEEACH", "SALES"]].dropna()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("Computing Inertia for K = 1 to 10...")
    for k in range(1, 11):
        km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(X_scaled)
        print(f"  K = {k:2d} | Inertia (WCSS): {km.inertia_:.2f}")

    k_choice = 3
    print(f"\nClustering with chosen K = {k_choice}...")
    kmeans = KMeans(n_clusters=k_choice, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    X_res = X.copy()
    X_res["Cluster"] = labels
    print("K-Means Cluster Counts:\n", X_res["Cluster"].value_counts().sort_index())

    hier = AgglomerativeClustering(n_clusters=k_choice)
    X_res["Hierarchical"] = hier.fit_predict(X_scaled)
    print("Hierarchical Cluster Counts:\n", X_res["Hierarchical"].value_counts().sort_index())

# =============================================================
# INTERACTIVE EXECUTION MENU
# =============================================================
if __name__ == "__main__":
    while True:
        print("\n==========================================")
        print("    ML PRACTICAL CODE EXECUTION MENU      ")
        print("==========================================")
        print("1. ML Practical 1: Uber Fare Price Prediction (Regression)")
        print("2. ML Practical 2: Email Spam Detection (KNN vs SVM)")
        print("3. ML Practical 3: Bank Customer Churn (Neural Network)")
        print("4. ML Practical 4: Diabetes Diagnosis (KNN)")
        print("5. ML Practical 5: Customer Sales Clustering (K-Means & Hierarchical)")
        print("0. Exit")
        ch = input("Select an option (0-5): ").strip()
        if ch == "1": run_ml1()
        elif ch == "2": run_ml2()
        elif ch == "3": run_ml3()
        elif ch == "4": run_ml4()
        elif ch == "5": run_ml5()
        elif ch == "0": break
        else: print("Invalid option.")
