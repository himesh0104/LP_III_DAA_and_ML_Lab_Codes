# -*- coding: utf-8 -*-
"""
ML PRACTICAL 1: UBER FARE PRICE PREDICTION (LINEAR & RANDOM FOREST REGRESSION)
Savitribai Phule Pune University (SPPU) - LP-III

================================================================================
LAB TEST DEMO INSTRUCTIONS & HOW TO RUN:
================================================================================
1. Make sure 'uber.csv' is in the current directory or parent directory.
2. Run the program:
       python ML_Practical_1_Uber_Fare_Prediction.py

The script automatically executes:
    - Data Cleaning & Preprocessing (Date parsing, filtering coordinates)
    - Outlier Detection using Interquartile Range (IQR)
    - Correlation Matrix Calculation & Heatmap Generation (Saved as PNG)
    - Linear Regression Training & Evaluation
    - Random Forest Regressor Training & Evaluation
    - Comparison of R2 Score, RMSE, and MAE

Bonus Interactive Fare Predictor:
    Enter hour [Demo: 14]: 14
    Enter day [Demo: 15]: 15
    Enter month [Demo: 6]: 6
    Enter pickup longitude [Demo: -73.98]: -73.98
    Enter pickup latitude [Demo: 40.75]: 40.75
    Enter dropoff longitude [Demo: -73.99]: -73.99
    Enter dropoff latitude [Demo: 40.74]: 40.74
    (Or press Enter to auto-run the demo ride prediction!)
================================================================================
"""
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

def locate_file(filename):
    for candidate in [filename, os.path.join("..", filename), os.path.join(".", filename)]:
        if os.path.exists(candidate):
            return candidate
    raise FileNotFoundError(f"Cannot find '{filename}'. Ensure the dataset is present.")

def main():
    print("=" * 75)
    print(" ML PRACTICAL 1: UBER FARE PREDICTION (LINEAR & RANDOM FOREST)")
    print("=" * 75)

    csv_path = locate_file("uber.csv")
    print(f">> Loading dataset from: {csv_path} ...")
    t0 = time.time()
    df = pd.read_csv(csv_path)
    print(f">> Loaded {len(df)} records in {time.time()-t0:.2f}s")

    # 1. Preprocessing
    print("\n--- 1. Data Cleaning & Feature Extraction ---")
    df = df.dropna().drop_duplicates()
    df = df.drop(columns=["Unnamed: 0", "key"], errors="ignore")

    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"], errors="coerce", utc=True)
    df = df.dropna(subset=["pickup_datetime"])

    df["hour"] = df["pickup_datetime"].dt.hour
    df["day"] = df["pickup_datetime"].dt.day
    df["month"] = df["pickup_datetime"].dt.month
    df = df.drop(columns=["pickup_datetime"])

    # Filter invalid coordinates & non-positive fares
    df = df[
        (df["fare_amount"] > 0) &
        df["pickup_longitude"].between(-180, 180) &
        df["dropoff_longitude"].between(-180, 180) &
        df["pickup_latitude"].between(-90, 90) &
        df["dropoff_latitude"].between(-90, 90)
    ]

    # 2. Outlier Detection using IQR
    print("\n--- 2. Outlier Identification via IQR ---")
    Q1 = df["fare_amount"].quantile(0.25)
    Q3 = df["fare_amount"].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = max(0, Q1 - 1.5 * IQR)
    upper_bound = Q3 + 1.5 * IQR

    outliers_count = len(df[(df["fare_amount"] < lower_bound) | (df["fare_amount"] > upper_bound)])
    print(f"   Fare Q1 = {Q1:.2f}, Q3 = {Q3:.2f}, IQR = {IQR:.2f}")
    print(f"   Valid fare range: [{lower_bound:.2f}, {upper_bound:.2f}]")
    print(f"   Identified outliers: {outliers_count}")

    df_clean = df[df["fare_amount"].between(lower_bound, upper_bound)]
    print(f"   Dataset size after outlier removal: {len(df_clean)} rows")

    # 3. Correlation & Heatmap
    print("\n--- 3. Correlation Analysis ---")
    numeric_df = df_clean.select_dtypes(include=[np.number])
    corr = numeric_df.corr()["fare_amount"].sort_values(ascending=False)
    print("   Correlation with Fare Amount:")
    for col, val in corr.items():
        print(f"     * {col:<20}: {val:+.4f}")

    # Generate and save heatmap plot
    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap - Uber Fare Dataset")
    heatmap_file = "uber_correlation_heatmap.png"
    plt.savefig(heatmap_file, dpi=200, bbox_inches="tight")
    print(f">> Heatmap plot saved as '{heatmap_file}'")
    plt.close()

    # 4. Model Training & Evaluation
    print("\n--- 4. Model Training & Evaluation ---")
    X = df_clean.drop(columns=["fare_amount", "passenger_count"], errors="ignore")
    y = df_clean["fare_amount"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"   Train samples: {len(X_train)}, Test samples: {len(X_test)}")

    # Fast & accurate Random Forest configuration
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest Regressor": RandomForestRegressor(n_estimators=50, max_depth=12, random_state=42, n_jobs=-1)
    }

    results = {}
    for name, model in models.items():
        print(f"   Training {name}...")
        t_start = time.time()
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        t_dur = time.time() - t_start

        r2 = r2_score(y_test, pred)
        rmse = np.sqrt(mean_squared_error(y_test, pred))
        mae = mean_absolute_error(y_test, pred)
        results[name] = {"R2": r2, "RMSE": rmse, "MAE": mae, "Time": t_dur}

    print("\n" + "=" * 75)
    print(f"{'Model':<25}{'R2 Score':<15}{'RMSE ($)':<15}{'MAE ($)':<15}{'Time (s)':<10}")
    print("-" * 75)
    for name, m in results.items():
        print(f"{name:<25}{m['R2']:<15.4f}{m['RMSE']:<15.4f}{m['MAE']:<15.4f}{m['Time']:<10.2f}")
    print("=" * 75)

    # 5. Interactive Ride Prediction Demo
    print("\n--- 5. Test Sample Ride Fare Prediction ---")
    print("[LAB TEST DEMO: Hour: 14, Day: 15, Month: 6, Long1: -73.98, Lat1: 40.75, Long2: -73.99, Lat2: 40.74]")
    demo_in = input("Press ENTER to run sample prediction (or type 'custom' to enter values): ").strip().lower()

    if demo_in == "custom":
        h = float(input("  Enter pickup hour (0-23): "))
        d = float(input("  Enter pickup day (1-31): "))
        m = float(input("  Enter pickup month (1-12): "))
        p_long = float(input("  Enter pickup longitude (e.g. -73.98): "))
        p_lat = float(input("  Enter pickup latitude (e.g. 40.75): "))
        d_long = float(input("  Enter dropoff longitude (e.g. -73.99): "))
        d_lat = float(input("  Enter dropoff latitude (e.g. 40.74): "))
    else:
        h, d, m = 14.0, 15.0, 6.0
        p_long, p_lat = -73.98, 40.75
        d_long, d_lat = -73.99, 40.74

    sample = pd.DataFrame([[p_long, p_lat, d_long, d_lat, h, d, m]], columns=X.columns)
    rf_model = models["Random Forest Regressor"]
    predicted_fare = rf_model.predict(sample)[0]
    print(f">> Predicted Fare for Ride: ${predicted_fare:.2f}")
    print("=" * 75)

if __name__ == "__main__":
    main()
