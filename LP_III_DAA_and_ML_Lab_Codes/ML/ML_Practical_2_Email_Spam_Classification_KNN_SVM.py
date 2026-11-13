# -*- coding: utf-8 -*-
"""
ML PRACTICAL 2: EMAIL SPAM CLASSIFICATION (KNN & SVM)
Savitribai Phule Pune University (SPPU) - LP-III

================================================================================
LAB TEST DEMO INSTRUCTIONS & HOW TO RUN:
================================================================================
1. Make sure 'emails.csv' is present in current directory or parent directory.
2. Run the program:
       python ML_Practical_2_Email_Spam_Classification_KNN_SVM.py

The script automatically executes:
    - Reads 5,172 email vectors across 3,000 word-frequency features
    - Separates features (X) and spam label (y: 1=Spam, 0=Not Spam)
    - Splits dataset into 80% Train and 20% Test (Stratified)
    - Feature Scaling via StandardScaler
    - Trains K-Nearest Neighbors (KNN with k=5)
    - Trains Support Vector Machine (Linear SVM)
    - Computes and prints:
        * Accuracy Score
        * Confusion Matrix
        * Classification Report (Precision, Recall, F1-Score)
        * Comprehensive Comparative Summary
================================================================================
"""
import os
import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def locate_file(filename):
    for candidate in [filename, os.path.join("..", filename), os.path.join(".", filename)]:
        if os.path.exists(candidate):
            return candidate
    raise FileNotFoundError(f"Cannot find '{filename}'. Ensure the dataset is present.")

def main():
    print("=" * 75)
    print(" ML PRACTICAL 2: EMAIL SPAM DETECTION USING KNN & SVM")
    print("=" * 75)

    csv_path = locate_file("emails.csv")
    print(f">> Loading dataset from: {csv_path} ...")
    t0 = time.time()
    df = pd.read_csv(csv_path)
    print(f">> Loaded dataset with shape {df.shape} in {time.time()-t0:.2f}s")

    # 1. Feature Separation
    df = df.drop_duplicates()
    target = "Prediction"
    X = df.drop(columns=[target, "Email No."], errors="ignore")
    y = df[target]

    spam_count = (y == 1).sum()
    ham_count = (y == 0).sum()
    print(f">> Class Distribution: Ham (0) = {ham_count}, Spam (1) = {spam_count}")

    # 2. Train-Test Split (80/20 Stratified)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Standardization
    print(">> Normalizing features using StandardScaler...")
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 4. Train Models
    models = {
        "K-Nearest Neighbors (KNN, k=5)": KNeighborsClassifier(n_neighbors=5),
        "Support Vector Machine (Linear SVM)": SVC(kernel="linear", random_state=42)
    }

    metrics = {}
    for name, model in models.items():
        print(f"\nTraining {name}...")
        t_start = time.time()
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        dur = time.time() - t_start

        acc = accuracy_score(y_test, preds)
        cm = confusion_matrix(y_test, preds)
        cr = classification_report(y_test, preds, zero_division=0)

        metrics[name] = {"acc": acc, "cm": cm, "cr": cr, "time": dur}

        print(f"--- {name} Results (Trained in {dur:.2f}s) ---")
        print(f"Accuracy: {acc * 100:.2f}%")
        print("Confusion Matrix:")
        print(f"  [TN={cm[0][0]:<4}  FP={cm[0][1]:<4}]")
        print(f"  [FN={cm[1][0]:<4}  TP={cm[1][1]:<4}]")
        print("\nClassification Report:")
        print(cr)

    # 5. Comparative Summary
    print("=" * 75)
    print("MODEL PERFORMANCE COMPARISON SUMMARY:")
    print("-" * 75)
    print(f"{'Model':<38}{'Accuracy':<15}{'Training Time':<15}")
    print("-" * 75)
    for name, m in metrics.items():
        print(f"{name:<38}{m['acc']*100:.2f}%{'':<9}{m['time']:.2f}s")
    print("-" * 75)
    print("CONCLUSION FOR VIVA:")
    print("  * SVM significantly outperforms KNN because high-dimensional word vectors")
    print("    (3000 dimensions) suffer from the 'Curse of Dimensionality' in distance-based KNN,")
    print("    whereas SVM finds an optimal separating hyperplane effectively in high dimensions.")
    print("=" * 75)

if __name__ == "__main__":
    main()
