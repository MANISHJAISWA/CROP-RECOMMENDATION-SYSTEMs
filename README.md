# 🌱 Crop Recommendation System

## 📌 Project Description

The **Crop Recommendation System** is a Machine Learning-based web application that recommends the most suitable crop based on soil and environmental conditions.

The system uses a **Random Forest Classifier** trained on the Crop Recommendation dataset. Users can enter important agricultural parameters such as Nitrogen, Phosphorus, Potassium, temperature, humidity, soil pH, and rainfall. The trained machine learning model analyzes these parameters and predicts a suitable crop.

This project aims to demonstrate how Machine Learning can be applied to agriculture to support data-driven crop selection.

---

## 🎯 Objectives

* Recommend suitable crops based on soil conditions.
* Use Machine Learning for agricultural prediction.
* Analyze important soil and environmental parameters.
* Provide a simple and user-friendly web interface.
* Demonstrate the practical use of the Random Forest algorithm.

---

## 🚀 Features

* 🌱 Crop recommendation using Machine Learning
* 🧪 Nitrogen, Phosphorus and Potassium input
* 🌡️ Temperature input
* 💧 Humidity input
* 🧑‍🌾 Soil pH input
* 🌧️ Rainfall input
* 🤖 Random Forest Classification
* 🌐 Flask-based web application
* 📱 Responsive user interface
* ⚡ Fast crop prediction

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Random Forest Classifier

### Data Processing

* Pandas
* NumPy

### Web Development

* Flask
* HTML
* CSS

### Dataset

* Kaggle Crop Recommendation Dataset

---

## 📊 Input Parameters

The model uses seven input parameters:

| Parameter   | Description                |
| ----------- | -------------------------- |
| N           | Nitrogen content in soil   |
| P           | Phosphorus content in soil |
| K           | Potassium content in soil  |
| Temperature | Temperature in °C          |
| Humidity    | Relative humidity          |
| pH          | Soil pH value              |
| Rainfall    | Rainfall in mm             |

The target variable is:

```text
label
```

which represents the crop recommended by the dataset.

---

## 🧠 Machine Learning Algorithm

### Random Forest Classifier

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to make predictions.

In this project:

```text
Input Soil & Weather Data
          ↓
Data Preprocessing
          ↓
Random Forest Classifier
          ↓
Crop Prediction
          ↓
Recommended Crop
```

---

## 📂 Project Structure

```text
CropRecommendation/
│
├── Crop_recommendation.csv
│
├── train_model.py
├── app.py
│
├── model/
│   └── crop_model.pkl
│
├── web_pages/
│   └── home.html
│
└── assets/
    └── style.css
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd CropRecommendation
```

### 3. Install required libraries

```bash
pip install pandas numpy scikit-learn flask
```

---

## ▶️ How to Run

### Step 1: Train the model

Run:

```bash
python train_model.py
```

This trains the Random Forest model and creates:

```text
model/crop_model.pkl
```

### Step 2: Start the Flask application

```bash
python app.py
```

### Step 3: Open the application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🖥️ Working

1. User opens the Crop Recommendation System.
2. User enters soil and environmental information.
3. Flask receives the input values.
4. The values are converted into a Pandas DataFrame.
5. The trained Random Forest model processes the input.
6. The model predicts the suitable crop.
7. The recommended crop is displayed on the website.

---

## 📈 Example

Example input:

```text
Nitrogen:     90
Phosphorus:   42
Potassium:    43
Temperature:  20.8 °C
Humidity:     82 %
Soil pH:      6.5
Rainfall:     203 mm
```

The system sends these values to the trained model and displays the predicted crop.

---

## 🔮 Future Scope

The project can be further enhanced by adding:

* 🌦️ Real-time weather API
* 🌾 Fertilizer recommendation
* 💧 Irrigation recommendation
* 🗺️ Location-based crop recommendation
* 📊 Prediction history
* 👨‍🌾 Farmer login and registration
* 🗄️ MySQL database
* 📱 Mobile application
* 📈 Data visualization dashboard
* 🤖 Comparison of multiple ML algorithms
* 🌱 Crop disease detection

---

## ⚠️ Disclaimer

This project is developed for **educational and demonstration purposes**. The predictions are based on the training dataset and should not be treated as a substitute for professional agricultural advice or local agronomic assessment.

---

## 👨‍💻 Author

**Manish Jaiswal**

B.Tech – Artificial Intelligence & Machine Learning

---

## ⭐ Acknowledgement

The project uses a publicly available **Crop Recommendation dataset from Kaggle** for machine learning experimentation and educational purposes.

---

## 📜 License

This project is intended for educational purposes. Check the original dataset's Kaggle license and terms before redistributing the dataset.
