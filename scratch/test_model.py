import pickle
import numpy as np
import pandas as pd

# Load assets
model = pickle.load(open('model.pkl', 'rb'))
# Workaround for scikit-learn version mismatch if needed
if hasattr(model, 'estimators_'):
    for estimator in model.estimators_:
        if not hasattr(estimator, 'monotonic_cst'):
            setattr(estimator, 'monotonic_cst', None)

mx = pickle.load(open('minmaxscaler.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))

# Rice sample from CSV (Row 0)
# N,P,K,temperature,humidity,ph,rainfall
rice_sample = np.array([[90, 42, 43, 20.87974371, 82.00274423, 6.502985292, 202.9355362]])

print("--- Testing Prediction Logic ---")

# 1. Current app.py logic (Only Standard Scaler)
try:
    sc_only = sc.transform(rice_sample)
    pred_sc = model.predict(sc_only)
    print(f"Prediction with only StandardScaler: {pred_sc[0]}")
except Exception as e:
    print(f"Error sc_only: {e}")

# 2. Notebook sequence (MinMax then Standard)
try:
    mx_transformed = mx.transform(rice_sample)
    both_transformed = sc.transform(mx_transformed)
    pred_both = model.predict(both_transformed)
    print(f"Prediction with MinMax + Standard: {pred_both[0]}")
except Exception as e:
    print(f"Error both: {e}")

# 3. No scaling (just in case the model was trained on raw data)
try:
    pred_raw = model.predict(rice_sample)
    print(f"Prediction with NO scaling: {pred_raw[0]}")
except Exception as e:
    print(f"Error raw: {e}")

# 4. Only MinMax
try:
    mx_only = mx.transform(rice_sample)
    pred_mx = model.predict(mx_only)
    print(f"Prediction with only MinMaxScaler: {pred_mx[0]}")
except Exception as e:
    print(f"Error mx_only: {e}")

crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
             8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
             14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
             19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

print("\n--- Mapping ---")
print(f"Target: Rice (1)")
