import pandas as pd
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# ---------------------------------
# Load Processed Dataset
# ---------------------------------

X_train = pd.read_csv(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\X_train.csv"
)

X_test = pd.read_csv(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\X_test.csv"
)

y_train = pd.read_csv(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\y_train.csv"
).values.ravel()

y_test = pd.read_csv(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\y_test.csv"
).values.ravel()

print("Processed datasets loaded successfully!")

# ---------------------------------
# Train Model
# ---------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# ---------------------------------
# Prediction
# ---------------------------------

y_pred = model.predict(X_test)

# ---------------------------------
# Accuracy
# ---------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy : {:.2f}%".format(accuracy*100))

# ---------------------------------
# Confusion Matrix
# ---------------------------------

print("\nConfusion Matrix\n")

print(confusion_matrix(y_test, y_pred))

# ---------------------------------
# Classification Report
# ---------------------------------

print("\nClassification Report\n")

print(classification_report(y_test, y_pred))

# ---------------------------------
# Save Model
# ---------------------------------

os.makedirs(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\models",
    exist_ok=True
)

joblib.dump(
    model,
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\models\hr_attrition_model.pkl"
)

print("\nModel Saved Successfully!")

print("\nLocation:")

print(r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\models\hr_attrition_model.pkl")