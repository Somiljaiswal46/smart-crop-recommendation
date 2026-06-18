<h1 align="center">🌾 AgriPulse: Intelligent Crop Recommendation Engine</h1>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel">
</div>

<br>

<p align="center">
  An advanced AI-powered web application that recommends the most optimal crop to grow based on soil composition and environmental data. Engineered for maximum yield and sustainability.
</p>

## 🌟 Live Demo
**[🚀 Try the Live Application Here](https://smart-crop-recommendation-tau.vercel.app/)**  
*(Click the link above to view the live project)*

---

## 📸 Preview
<div align="center">
  <img width="1893" height="897" alt="Screenshot 2026-06-18 212643" src="https://github.com/user-attachments/assets/12aeb38c-9996-4db4-812d-fcc4777b07c6" />

  <br><br>
  <b>🎯 22 Crop Types &nbsp;&nbsp;|&nbsp;&nbsp; 📈 99.3% Model Accuracy &nbsp;&nbsp;|&nbsp;&nbsp; 📊 2,200 Training Samples</b>
</div>

---

## 🚀 Features
- **Highly Accurate Predictions:** Achieved **99.3%** accuracy using state-of-the-art Machine Learning models.
- **Modern User Interface:** A sleek, premium, and fully responsive web UI tailored for precision agriculture.
- **Real-Time Analysis:** Instant, AI-driven recommendations based on comprehensive soil test reports.
- **Cloud Deployed:** Seamlessly hosted and available globally via Vercel.

## 🛠️ Tech Stack
- **Backend:** Python 3, Flask
- **Machine Learning:** Scikit-Learn, Pandas, NumPy
- **Frontend:** HTML5, CSS3, JavaScript
- **Deployment:** Vercel

---

## 🧠 How It Works
The recommendation engine analyzes **7 key environmental and soil parameters**:
1. **Nitrogen (N)** ratio in soil
2. **Phosphorus (P)** ratio in soil
3. **Potassium (K)** ratio in soil
4. **Temperature** (in °C)
5. **Humidity** (in %)
6. **pH Value** of the soil
7. **Rainfall** (in mm)

Based on these measured inputs, the trained ML model instantly predicts the most suitable crop for your specific conditions out of 22 different categories.

---

## 💻 Local Installation & Setup

To run this project on your local machine, follow these steps:

**1. Clone the repository**
```bash
git clone https://github.com/Somiljaiswal46/smart-crop-recommendation.git
cd smart-crop-recommendation
```

**2. Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the Application**
```bash
python app.py
```
*The app will start running locally at `http://127.0.0.1:5000/`*

---

## 📂 Project Structure
```text
📦 smart-crop-recommendation
 ┣ 📂 static             # CSS, JS, and image assets
 ┣ 📂 templates          # HTML templates for the web interface
 ┣ 📜 app.py             # Main Flask application and API endpoints
 ┣ 📜 model.pkl          # Trained Machine Learning Model
 ┣ 📜 standscaler.pkl    # Standard Scaler object
 ┣ 📜 minmaxscaler.pkl   # MinMax Scaler object
 ┣ 📜 requirements.txt   # Python dependencies required
 ┣ 📜 vercel.json        # Configuration for Vercel deployment
 ┗ 📜 README.md          # Project Documentation
```

---

<div align="center">
  <b>Developed with ❤️ by <a href="https://github.com/Somiljaiswal46">Somil Jaiswal</a></b>
</div>
