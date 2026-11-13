# -*- coding: utf-8 -*-
"""
ML PRACTICAL 4: DIABETES CLASSIFICATION USING KNN (MEDICAL DATA PREPROCESSING)
Savitribai Phule Pune University (SPPU) - LP-III

================================================================================
LAB TEST DEMO INSTRUCTIONS & HOW TO RUN:
================================================================================
1. Make sure 'diabetes.csv' is present in current directory or parent directory.
2. Run the program:
       python ML_Practical_4_Diabetes_Classification_KNN.py

The script automatically executes:
    - Reads 768 patient medical records
    - Identifies invalid zero measurements in medical attributes:
      ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    - Replaces biologically impossible zero values with column medians
    - Splits dataset into 80% Train and 20% Test
    - Scales features using StandardScaler
    - Trains K-Nearest Neighbors Classifier (k=5)
    - Computes and displays:
        * Confusion Matrix
        * Accuracy Score (~75.3%)
        * Error Rate (1 - Accuracy) (~24.7%)
        * Precision Score (~68.8%)
        * Recall Score (Sensitivity) (~55.6%)

Bonus Interactive Diagnosis Demo:
    Patient Demo: Pregnancies: 2, Glucose: 138, BloodPressure: 62,
                  SkinThickness: 35, Insulin: 120, BMI: 33.6, DPF: 0.127, Age: 47
    (Press ENTER to run the demo patient prediction!)
================================================================================
"""
import os
import time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

def locate_file(filename):
    for candidate in [filename, os.path.join("..", filename), os.path.join(".", filename)]:
        if os.path.exists(candidate):
            return candidate
    raise FileNotFoundError(f"Cannot find '{filename}'. Ensure the dataset is present.")

def main():
    print("=" * 75)
    print(" ML PRACTICAL 4: DIABETES DIAGNOSIS USING KNN CLASSIFIER")
    print("=" * 75)

    csv_path = locate_file("diabetes.csv")
    print(f">> Loading dataset from: {csv_path} ...")
    df = pd.read_csv(csv_path)
    df = df.drop_duplicates()
    print(f">> Loaded {len(df)} patient records.")

    # 1. Handling Invalid Medical Zeros
    print("\n--- 1. Handling Biologically Impossible Zero Values ---")
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    zero_cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    for col in zero_cols:
        if col in X.columns:
            zero_count = (X[col] == 0).sum()
            med_val = X[X[col] != 0][col].median()
            X[col] = X[col].replace(0, med_val)
            print(f"   * Replaced {zero_count:>3} invalid zeros in '{col}' with median {med_val:.1f}")

    # 2. Train-Test Split (80/20 Stratified)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Standardization
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 4. Train KNN Classifier
    print("\n--- 2. Training KNN Model (k=5) ---")
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # 5. Model Evaluation Metrics
    acc = accuracy_score(y_test, y_pred)
    error_rate = 1.0 - acc
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    cm = confusion_matrix(y_test, y_pred)

    print("\n" + "=" * 75)
    print("EVALUATION METRICS (REQUIRED FOR LAB REPORT & VIVA):")
    print("-" * 75)
    print(f"1. Accuracy Score:  {acc:.4f}  ({acc * 100:.2f}%)")
    print(f"2. Error Rate:      {error_rate:.4f}  ({error_rate * 100:.2f}%)  [Formula: 1 - Accuracy]")
    print(f"3. Precision Score: {prec:.4f}  ({prec * 100:.2f}%)  [Formula: TP / (TP + FP)]")
    print(f"4. Recall Score:    {rec:.4f}  ({rec * 100:.2f}%)  [Formula: TP / (TP + FN)]")
    print(f"5. F1-Score:        {f1:.4f}  ({f1 * 100:.2f}%)")
    print("-" * 75)
    print("Confusion Matrix:")
    print(f"               Predicted Non-Diabetic (0)    Predicted Diabetic (1)")
    print(f"Actual Non-Diab (0)        TN = {cm[0][0]:<4}                  FP = {cm[0][1]:<4}")
    print(f"Actual Diabetic (1)        FN = {cm[1][0]:<4}                  TP = {cm[1][1]:<4}")
    print("=" * 75)

    # 6. Interactive Patient Test Demo
    print("\n--- 3. Patient Diagnosis Test Demo ---")
    print("[DEMO VALUES: Preg:2, Gluc:138, BP:62, Skin:35, Ins:120, BMI:33.6, DPF:0.127, Age:47]")
    raw_in = input("Press ENTER to run patient demo diagnosis (or type 'custom'): ").strip().lower()

    if raw_in == "custom":
        p_vals = []
        for col in X.columns:
            p_vals.append(float(input(f"  Enter {col}: ")))
    else:
        p_vals = [2.0, 138.0, 62.0, 35.0, 120.0, 33.6, 0.127, 47.0]

    sample_patient = pd.DataFrame([p_vals], columns=X.columns)
    sample_sc = scaler.transform(sample_patient)
    diag = model.predict(sample_sc)[0]
    prob_diab = model.predict_proba(sample_sc)[0][1]

    verdict = "POSITIVE FOR DIABETES (Diabetic Risk Detected)" if diag == 1 else "NEGATIVE (Non-Diabetic)"
    print(f"\n>> Diagnosis Result: {verdict}")
    print(f">> Confidence Probability of Diabetes: {prob_diab * 100:.2f}%")
    print("=" * 75)

if __name__ == "__main__":
    main()
