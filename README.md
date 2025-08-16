# Waste Recycling Rate Prediction

This project predicts the **Recycling Rate (%)** for different cities/districts based on waste management and demographic data.  
The pipeline includes **data preprocessing, exploratory data analysis (EDA), model training (with algorithm comparison & hyperparameter tuning)**, and a **Flask API** for serving predictions.

---

## 📂 Project Structure

```
project_root/
├── Notebooks/
│   ├── data_preparation.ipynb       # Data cleaning & preprocessing
│   ├── exploratory_data_analysis.ipynb # Data visualization & insights
│   ├── model_training.ipynb         # Model training & evaluation
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── preprocess.py            # Preprocessing functions/classes
│   ├── models/
│   │   ├── __init__.py
│   │   ├── train.py                  # Model training logic
│   │   ├── predict.py                # Prediction functions
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py                 # Utility functions
│   ├── app.py                         # Flask API for serving predictions
├── data/
│   ├── raw/                           # Raw dataset (train.csv, test.csv)
│   ├── processed/                     # Processed datasets
├── models/
│   ├── trained_model.pkl               # Saved model
├── static/                             # Static files for Flask app
├── templates/                          # HTML templates for Flask app
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
├── predictions.csv                     # Model predictions
└── report.pdf                          # Project report
```

---

## ⚙️ Environment Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/waste-recycling-prediction.git
cd waste-recycling-prediction
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```

Activate it:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 📊 Running the Project

### **Step 1: Data Preprocessing**
Run:
```bash
jupyter notebook Notebooks/data_preparation.ipynb
```
This cleans and encodes the data, saving preprocessed datasets in `data/processed/` and encoders in `models/`.

---

### **Step 2: Exploratory Data Analysis**
Run:
```bash
jupyter notebook Notebooks/exploratory_data_analysis.ipynb
```
Generates visual insights like feature distributions, correlations, and trends.

---

### **Step 3: Model Training**
Run:
```bash
jupyter notebook Notebooks/model_training.ipynb
```
- Compares multiple regression algorithms.
- Selects the best (Lasso Regression in this case).
- Saves the trained model as `models/trained_model.pkl`.

---

### **Step 4: Flask API for Predictions**
Run:
```bash
python src/app.py
```
The API will be available at:
```
http://127.0.0.1:5000/
```

---

## 📤 Making Predictions
Once the Flask app is running, you can send a POST request with JSON data:

```json
{
  "City/District": "Mumbai",
  "Waste Type": "Plastic",
  "Waste Generated (Tons/Day)": 200,
  "Population Density (People/km²)": 30000,
  "Municipal Efficiency Score (1-10)": 8,
  "Disposal Method": "Recycling",
  "Cost of Waste Management (₹/Ton)": 1200,
  "Awareness Campaigns Count": 5,
  "Landfill Capacity (Tons)": 5000,
  "Year": 2025,
  "Landfill Lat": 19.07,
  "Landfill Lon": 72.87
}
```

You’ll receive:
```json
{"predicted_recycling_rate": 45.32}
```

---

## 🛠 Dependencies
Main Python libraries:
- pandas
- numpy
- scikit-learn
- category_encoders
- matplotlib
- seaborn
- flask
- joblib
- jupyter

Install all with:
```bash
pip install -r requirements.txt
```

---

## 📌 Notes
- Ensure your `waste_data.csv` is inside `data/raw/`.
- Model and encoders are automatically saved in the `models/` folder.
- The best model (Lasso Regression) was chosen after testing multiple regression algorithms.

---

## 👨‍💻 Author
- **Harsh**
