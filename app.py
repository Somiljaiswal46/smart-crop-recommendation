from flask import Flask, request, render_template
import numpy as np
import pandas
import sklearn
import pickle

# Dynamically locate the crop image in static/crops/
import os

def get_crop_image_url(crop_name):
    if not crop_name:
        return "/static/crop.png"
    
    # Normalize class name: lowercase, stripped
    crop_lower = crop_name.strip().lower()
    
    # Check for .jpg
    jpg_path = os.path.join("static", "crops", f"{crop_lower}.jpg")
    if os.path.exists(jpg_path):
        return f"/static/crops/{crop_lower}.jpg"
        
    # Check for .png
    png_path = os.path.join("static", "crops", f"{crop_lower}.png")
    if os.path.exists(png_path):
        return f"/static/crops/{crop_lower}.png"
        
    # Fallback to the default crop placeholder
    return "/static/crop.png"


model = pickle.load(open('model.pkl','rb'))

# Workaround for scikit-learn version mismatch when loading the pickled model
if hasattr(model, 'estimators_'):
    for estimator in model.estimators_:
        if not hasattr(estimator, 'monotonic_cst'):
            setattr(estimator, 'monotonic_cst', None)

sc = pickle.load(open('minmaxscaler.pkl','rb'))


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    N = float(request.form['Nitrogen'])
    P = float(request.form['Phosporus'])
    K = float(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['pH'])
    rainfall = float(request.form['Rainfall'])

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)
    sc_features = sc.transform(single_pred)
    prediction = model.predict(sc_features)

    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}
    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = "{} is the best crop to be cultivated right there".format(crop)
        crop_image = get_crop_image_url(crop)
    else:
        crop = ""
        crop_image = "/static/crop.png"
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
    return render_template('index.html', result=result, crop=crop, crop_image=crop_image)

if __name__ == "__main__":
    app.run(debug=True)