import pickle
import numpy as np
import pandas as pd

# Load model and new scaler
model = pickle.load(open('model.pkl', 'rb'))
if hasattr(model, 'estimators_'):
    for estimator in model.estimators_:
        if not hasattr(estimator, 'monotonic_cst'):
            setattr(estimator, 'monotonic_cst', None)

sc = pickle.load(open('standscaler.pkl', 'rb'))

# Load dataset
df = pd.read_csv('Crop_recommendation.csv')

def get_prediction(row):
    features = row.drop('label').values.astype(float).reshape(1, -1)
    transformed = sc.transform(features)
    pred = model.predict(transformed)[0]
    return pred

# Select one sample per unique crop to verify
verified_count = 0
failed_count = 0

crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
             8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
             14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
             19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

# Reverse dict for mapping dataset labels to numbers
dataset_label_map = {v.lower(): k for k, v in crop_dict.items()}

unique_labels = df['label'].unique()
for label in unique_labels:
    sample = df[df['label'] == label].iloc[0]
    pred_val = get_prediction(sample)
    expected_val = dataset_label_map[label]
    
    if pred_val == expected_val:
        verified_count += 1
    else:
        print(f"FAILED: Label={label}, Expected={expected_val}, Got={pred_val} ({crop_dict.get(pred_val, 'Unknown')})")
        failed_count += 1

print(f"\nVerification Results:")
print(f"Verified: {verified_count}/{len(unique_labels)}")
print(f"Failed: {failed_count}")
