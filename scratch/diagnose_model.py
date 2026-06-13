import pickle
import numpy as np
import pandas as pd

# Load everything
model = pickle.load(open('model.pkl', 'rb'))
mx = pickle.load(open('minmaxscaler.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))

# Load dataset
df = pd.read_csv('Crop_recommendation.csv')

def get_raw_prediction(row_idx):
    row = df.iloc[row_idx]
    features = row.drop('label').values.astype(float).reshape(1, -1)
    true_label = row['label']
    
    # Try different pipelines
    # 1. mx only
    pred_mx = model.predict(mx.transform(features))[0]
    
    # 2. mx + sc
    pred_mx_sc = model.predict(sc.transform(mx.transform(features)))[0]
    
    # 3. sc only (unlikely but worth a check)
    try:
        pred_sc = model.predict(sc.transform(features))[0]
    except:
        pred_sc = "Error"
    
    return true_label, pred_mx, pred_mx_sc, pred_sc

print("Diagnostics for various crops:")
indices = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100]
results = []
for idx in indices:
    true_l, p_mx, p_msc, p_s = get_raw_prediction(idx)
    results.append({'True': true_l, 'mx_only': p_mx, 'mx_sc': p_msc, 'sc_only': p_s})

print(pd.DataFrame(results))

# See what the unique classes are
if hasattr(model, 'classes_'):
    print(f"\nModel Classes: {model.classes_}")
