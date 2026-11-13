# -*- coding: utf-8 -*-
"""
ML PRACTICAL 5: CUSTOMER SALES CLUSTERING (K-MEANS & HIERARCHICAL WITH ELBOW)
Savitribai Phule Pune University (SPPU) - LP-III

================================================================================
LAB TEST DEMO INSTRUCTIONS & HOW TO RUN:
================================================================================
1. Make sure 'sales_data_sample.csv' is in current directory or parent directory.
2. Run the program:
       python ML_Practical_5_Sales_Clustering_KMeans.py

The script automatically executes:
    - Reads sales orders dataset using 'latin1' encoding
    - Selects features: ['QUANTITYORDERED', 'PRICEEACH', 'SALES']
    - Scales features with StandardScaler
    - Computes Inertia / WCSS for K = 1 to 10
    - Generates and saves Elbow Method Plot ('sales_elbow_plot.png')
    - Terminal Prompt:
          Enter optimal number of clusters [Demo: 3]: 3
          (Press ENTER to choose the optimal K = 3!)
    - Fits K-Means with K = 3 and displays cluster distributions
    - Fits Agglomerative (Hierarchical) Clustering with K = 3
    - Compares K-Means vs Hierarchical cluster segmentations
================================================================================
"""
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering

def locate_file(filename):
    for candidate in [filename, os.path.join("..", filename), os.path.join(".", filename)]:
        if os.path.exists(candidate):
            return candidate
    raise FileNotFoundError(f"Cannot find '{filename}'. Ensure the dataset is present.")

def main():
    print("=" * 75)
    print(" ML PRACTICAL 5: SALES DATA CLUSTERING (K-MEANS & HIERARCHICAL)")
    print("=" * 75)

    csv_path = locate_file("sales_data_sample.csv")
    print(f">> Loading dataset from: {csv_path} ...")
    df = pd.read_csv(csv_path, encoding="latin1")
    df = df.drop_duplicates()
    print(f">> Loaded {len(df)} sales records.")

    # 1. Feature Extraction & Scaling
    features = ["QUANTITYORDERED", "PRICEEACH", "SALES"]
    X = df[features].dropna()
    print(f">> Selected features: {features} ({len(X)} records)")

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 2. Elbow Method for Optimal K
    print("\n--- 1. Computing Elbow Method for K = 1 to 10 ---")
    inertia = []
    k_range = range(1, 11)

    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X_scaled)
        inertia.append(km.inertia_)
        print(f"   K = {k:>2}  ->  Inertia (WCSS) = {km.inertia_:>12.2f}")

    # Save Elbow Plot
    plt.figure(figsize=(8, 5))
    plt.plot(k_range, inertia, marker="o", color="b", linewidth=2)
    plt.xlabel("Number of Clusters (K)")
    plt.ylabel("Inertia (Within-Cluster Sum of Squares)")
    plt.title("Elbow Method For Optimal K (Sales Dataset)")
    plt.grid(True, linestyle="--", alpha=0.6)
    elbow_file = "sales_elbow_plot.png"
    plt.savefig(elbow_file, dpi=200, bbox_inches="tight")
    print(f">> Elbow method curve saved as '{elbow_file}'")
    plt.close()

    # 3. Interactive Cluster Selection
    print("\n" + "=" * 75)
    print("[LAB TEST DEMO DATA: By inspecting the elbow curve, the bend occurs at K = 3]")
    print("-" * 75)
    raw_k = input("Enter optimal number of clusters [Press Enter for demo: 3]: ").strip()
    k_optimal = int(raw_k) if raw_k else 3

    # 4. K-Means Clustering
    print(f"\n--- 2. Fitting K-Means Clustering with K = {k_optimal} ---")
    kmeans = KMeans(n_clusters=k_optimal, random_state=42, n_init=10)
    kmeans_labels = kmeans.fit_predict(X_scaled)

    X_result = X.copy()
    X_result["KMeans_Cluster"] = kmeans_labels

    print(f">> K-Means Cluster Distribution (K = {k_optimal}):")
    print(X_result["KMeans_Cluster"].value_counts().sort_index())

    print("\n>> Cluster Centroids (Mean Feature Values per Cluster):")
    cluster_means = X_result.groupby("KMeans_Cluster").mean()
    print(cluster_means.to_string())

    # 5. Hierarchical Clustering (Agglomerative)
    print(f"\n--- 3. Fitting Hierarchical Agglomerative Clustering (K = {k_optimal}) ---")
    hierarchical = AgglomerativeClustering(n_clusters=k_optimal)
    hier_labels = hierarchical.fit_predict(X_scaled)
    X_result["Hierarchical_Cluster"] = hier_labels

    print(f">> Hierarchical Cluster Distribution (K = {k_optimal}):")
    print(X_result["Hierarchical_Cluster"].value_counts().sort_index())

    # 6. Sample Output
    print("\n--- 4. Sample Clustered Records Preview ---")
    print(X_result.head(10).to_string())

    print("\n" + "=" * 75)
    print("VIVA EVALUATION TAKEAWAYS:")
    print("  * Elbow Method identifies K where adding another cluster yields diminishing")
    print("    returns in reducing inertia (variance). Here K = 3 represents Low, Medium,")
    print("    and High-volume sales transactions.")
    print("=" * 75)

if __name__ == "__main__":
    main()
