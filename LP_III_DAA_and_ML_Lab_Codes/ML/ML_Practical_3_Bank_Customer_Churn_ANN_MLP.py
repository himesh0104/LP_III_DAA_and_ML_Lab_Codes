# -*- coding: utf-8 -*-
"""
ML PRACTICAL 3: BANK CUSTOMER CHURN PREDICTION (NEURAL NETWORK / MLPCLASSIFIER)
Savitribai Phule Pune University (SPPU) - LP-III

================================================================================
LAB TEST DEMO INSTRUCTIONS & HOW TO RUN:
================================================================================
1. Make sure 'Churn_Modelling.csv' is in current directory or parent directory.
2. Run the program:
       python ML_Practical_3_Bank_Customer_Churn_ANN_MLP.py

The script automatically executes:
    - Reads 10,000 bank customer profiles
    - Removes non-predictive identifiers (RowNumber, CustomerId, Surname)
    - One-Hot Encodes categorical features (Geography, Gender)
    - Normalizes numerical features via StandardScaler
    - Builds Model 1 (Baseline MLP Neural Network: 1 hidden layer with 16 neurons)
    - Identifies hyperparameter tuning points
    - Builds Model 2 (Optimized MLP: 2 hidden layers (32, 16), ReLU, Adam, L2 reg)
    - Evaluates both models with Accuracy, Confusion Matrix, and Classification Report

Bonus Interactive Churn Prediction Demo:
    Customer Demo: CreditScore=650, Age=40, Tenure=5, Balance=75000,
                   NumOfProducts=2, HasCrCard=1, IsActiveMember=1, Salary=60000
    (Press ENTER to run the demo test!)
================================================================================
"""
import os
import time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def locate_file(filename):
    for candidate in [filename, os.path.join("..", filename), os.path.join(".", filename)]:
        if os.path.exists(candidate):
            return candidate
    raise FileNotFoundError(f"Cannot find '{filename}'. Ensure the dataset is present.")

def main():
    print("=" * 75)
    print(" ML PRACTICAL 3: BANK CUSTOMER CHURN PREDICTION (ARTIFICIAL NEURAL NET)")
    print("=" * 75)

    csv_path = locate_file("Churn_Modelling.csv")
    print(f">> Loading dataset from: {csv_path} ...")
    df = pd.read_csv(csv_path)
    print(f">> Loaded {len(df)} customer records.")

    # 1. Feature Preprocessing
    df = df.drop(columns=["RowNumber", "CustomerId", "Surname"], errors="ignore")
    X = df.drop("Exited", axis=1)
    y = df["Exited"]

    print(f">> Class Distribution: Retained (0) = {(y==0).sum()}, Exited (1) = {(y==1).sum()}")

    # One-Hot Encoding for categorical features
    X = pd.get_dummies(X, columns=["Geography", "Gender"], drop_first=True)
    feature_names = list(X.columns)

    # 2. Train-Test Split (80/20 Stratified)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Standardization
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 4. Model 1: Baseline Neural Network (Single Layer)
    print("\n--- Model 1: Baseline Neural Network (Hidden Layers: (16,)) ---")
    t0 = time.time()
    model1 = MLPClassifier(hidden_layer_sizes=(16,), max_iter=300, random_state=42)
    model1.fit(X_train, y_train)
    pred1 = model1.predict(X_test)
    acc1 = accuracy_score(y_test, pred1)
    print(f"Model 1 Trained in {time.time()-t0:.2f}s | Test Accuracy: {acc1 * 100:.2f}%")

    # 5. Model 2: Improved Deep Neural Network (Architecture: (32, 16), Adam, Early Stopping)
    print("\n--- Model 2: Optimized Deep Neural Network (Hidden Layers: (32, 16)) ---")
    t0 = time.time()
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
    acc2 = accuracy_score(y_test, pred2)
    cm2 = confusion_matrix(y_test, pred2)
    print(f"Model 2 Trained in {time.time()-t0:.2f}s | Test Accuracy: {acc2 * 100:.2f}%")

    print("\nConfusion Matrix (Model 2):")
    print(f"  [TN={cm2[0][0]:<4}  FP={cm2[0][1]:<4}]")
    print(f"  [FN={cm2[1][0]:<4}  TP={cm2[1][1]:<4}]")

    print("\nClassification Report (Model 2):")
    print(classification_report(y_test, pred2, zero_division=0))

    # 6. Interactive Prediction Demo
    print("=" * 75)
    print("SAMPLE CUSTOMER CHURN PREDICTION DEMO:")
    print("[DEMO VALUES: Credit: 650, Age: 40, Tenure: 5, Balance: 75000, Products: 2, CrCard: 1, Active: 1, Salary: 60000]")
    demo_in = input("Press ENTER to test demo customer churn prediction: ").strip()

    # Demo customer: France (Germany=0, Spain=0), Male (Gender_Male=1)
    sample_dict = {
        'CreditScore': 650, 'Age': 40, 'Tenure': 5, 'Balance': 75000.0,
        'NumOfProducts': 2, 'HasCrCard': 1, 'IsActiveMember': 1, 'EstimatedSalary': 60000.0,
        'Geography_Germany': 0, 'Geography_Spain': 0, 'Gender_Male': 1
    }
    sample_df = pd.DataFrame([sample_dict])[feature_names]
    sample_scaled = scaler.transform(sample_df)
    prob_churn = model2.predict_proba(sample_scaled)[0][1]
    churn_pred = model2.predict(sample_scaled)[0]

    status = "CHURN / EXIT RISK DETECTED" if churn_pred == 1 else "CUSTOMER RETAINED (LOYAL)"
    print(f"\n>> Churn Probability: {prob_churn * 100:.2f}%")
    print(f">> Prediction Verdict: {status}")
    print("=" * 75)

if __name__ == "__main__":
    main()
