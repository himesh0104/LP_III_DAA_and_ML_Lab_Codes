# -*- coding: utf-8 -*-
"""
Automated Test Runner inside LP_III_DAA_and_ML_Lab_Codes
Run: python test_all_practicals.py
"""
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCRIPTS = [
    (os.path.join(BASE_DIR, "DAA", "DAA_Practical_1_Fibonacci.py"), "8\n"),
    (os.path.join(BASE_DIR, "DAA", "DAA_Practical_2_Huffman_Encoding.py"), "\n"),
    (os.path.join(BASE_DIR, "DAA", "DAA_Practical_3_Fractional_Knapsack.py"), "\n"),
    (os.path.join(BASE_DIR, "DAA", "DAA_Practical_4_01_Knapsack_DP.py"), "\n"),
    (os.path.join(BASE_DIR, "DAA", "DAA_Practical_5_N_Queens_Backtracking.py"), "8\n"),
    (os.path.join(BASE_DIR, "ML", "ML_Practical_1_Uber_Fare_Prediction.py"), "\n"),
    (os.path.join(BASE_DIR, "ML", "ML_Practical_2_Email_Spam_Classification_KNN_SVM.py"), ""),
    (os.path.join(BASE_DIR, "ML", "ML_Practical_3_Bank_Customer_Churn_ANN_MLP.py"), "\n"),
    (os.path.join(BASE_DIR, "ML", "ML_Practical_4_Diabetes_Classification_KNN.py"), "\n"),
    (os.path.join(BASE_DIR, "ML", "ML_Practical_5_Sales_Clustering_KMeans.py"), "3\n"),
]

passed = 0
failed = 0

print("=" * 75)
print("RUNNING COMPLETE AUTOMATED CHECK ON ALL 10 PRACTICALS")
print("=" * 75)

for script_path, test_input in SCRIPTS:
    name = os.path.basename(script_path)
    cwd = os.path.dirname(script_path)
    print(f"[TESTING] {name} ...", end=" ", flush=True)
    proc = subprocess.Popen(
        [sys.executable, name],
        cwd=cwd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    stdout, stderr = proc.communicate(input=test_input, timeout=90)

    if proc.returncode == 0:
        print("[PASS]")
        passed += 1
    else:
        print(f"[FAIL - Code {proc.returncode}]")
        print("STDERR:\n", stderr)
        failed += 1

print("=" * 75)
print(f"RESULT: {passed} PASSED, {failed} FAILED out of 10 practicals.")
print("=" * 75)

