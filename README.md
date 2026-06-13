# Smart-Crop-Advisor 🌱

A Machine Learning-based precision agriculture tool that recommends the optimal crop to cultivate based on soil nutrients (N, P, K) and climatic conditions (Temperature, Humidity, pH, and Rainfall).

## 🚀 Deployment Instructions (Render)

To deploy this project to a public URL:

1. **Upload to GitHub**:
   - Create a new repository on GitHub named `Smart-Crop-Advisor`.
   - Upload all files from this folder to that repository.

2. **Connect to Render**:
   - Go to [Render.com](https://render.com) and create a free account.
   - Click **New +** and select **Web Service**.
   - Connect your GitHub account and select the `Smart-Crop-Advisor` repository.
   - **Configuration**:
     - **Runtime**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
   - Click **Deploy Web Service**.

3. **Your Link**:
   - Once the build is finished, Render will provide you with a public URL (e.g., `https://smart-crop-advisor.onrender.com`).

## 🛠️ Technology Stack
- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-Learn
- **Data Handling**: Pandas, Numpy
- **Frontend**: HTML/CSS (Glassmorphic Design)

## 📊 Features
- Predicts 22 different types of crops.
- Real-time soil and weather data input.
- Visual crop recommendations with images.