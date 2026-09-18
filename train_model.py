import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# ==========================================
# 1. LOAD DATASET
# ==========================================

data = pd.read_csv("Crop_recommendation.csv")

print("======================================")
print("Crop Recommendation System")
print("======================================")

print("\nDataset loaded successfully!")

print("\nFirst 5 rows:")
print(data.head())

print("\nDataset shape:")
print(data.shape)

print("\nColumns:")
print(data.columns)


# ==========================================
# 2. SELECT FEATURES
# ==========================================

X = data[
    [
        "N",
        "P",
        "K",
        "temperature",
        "humidity",
        "ph",
        "rainfall"
    ]
]


# ==========================================
# 3. TARGET VARIABLE
# ==========================================

y = data["label"]


# ==========================================
# 4. SPLIT DATASET
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)


# ==========================================
# 5. CREATE RANDOM FOREST MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ==========================================
# 6. TRAIN MODEL
# ==========================================

print("\nTraining model...")

model.fit(X_train, y_train)

print("Model training completed!")


# ==========================================
# 7. TEST MODEL
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 8. CALCULATE ACCURACY
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

print("\n======================================")
print("MODEL RESULTS")
print("======================================")

print("Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")


# ==========================================
# 9. CLASSIFICATION REPORT
# ==========================================

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ==========================================
# 10. CREATE MODEL FOLDER
# ==========================================

if not os.path.exists("model"):
    os.makedirs("model")


# ==========================================
# 11. SAVE MODEL
# ==========================================

with open("model/crop_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("\n======================================")
print("MODEL SAVED SUCCESSFULLY")
print("======================================")

print("File: model/crop_model.pkl")