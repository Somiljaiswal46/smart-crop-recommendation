import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# 1. Load the dataset
df = pd.read_csv('Crop_recommendation.csv')
df.dropna(inplace=True)

# 2. Define the mapping (must match app.py exactly)
crop_dict = {
    'rice': 1,
    'maize': 2,
    'jute': 3,
    'cotton': 4,
    'coconut': 5,
    'papaya': 6,
    'orange': 7,
    'apple': 8,
    'muskmelon': 9,
    'watermelon': 10,
    'grapes': 11,
    'mango': 12,
    'banana': 13,
    'pomegranate': 14,
    'lentil': 15,
    'blackgram': 16,
    'mungbean': 17,
    'mothbeans': 18,
    'pigeonpeas': 19,
    'kidneybeans': 20,
    'chickpea': 21,
    'coffee': 22
}

# 3. Preprocessing
df['label_num'] = df['label'].map(crop_dict)
df.dropna(subset=['label_num'], inplace=True) # Ensure no unmapped labels
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']].values  # numpy array
y = df['label_num'].astype(int).values

# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Scaling on numpy arrays (matches inference in app.py exactly)
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Training
model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
model.fit(X_train_scaled, y_train)

# 7. Evaluate
train_acc = model.score(X_train_scaled, y_train)
test_acc = model.score(X_test_scaled, y_test)
print(f"Training Accuracy: {train_acc:.4f}")
print(f"Testing Accuracy : {test_acc:.4f}")

# 8. Save artifacts
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(scaler, open('minmaxscaler.pkl', 'wb'))
print("New model.pkl and minmaxscaler.pkl saved.")

# 9. Verify multiple crops
reverse_dict = {v: k for k, v in crop_dict.items()}
test_crops = ['rice', 'coconut', 'orange', 'apple', 'mango', 'coffee']
print("\n--- Verification ---")
for crop_name in test_crops:
    sample = df[df['label'] == crop_name].iloc[0]
    features = np.array([[sample['N'], sample['P'], sample['K'],
                          sample['temperature'], sample['humidity'],
                          sample['ph'], sample['rainfall']]])
    scaled = scaler.transform(features)
    pred = model.predict(scaled)[0]
    status = 'OK' if reverse_dict[pred] == crop_name else 'WRONG'
    print(f"  [{status}] True: {crop_name.ljust(12)} Predicted: {reverse_dict[pred]}")
