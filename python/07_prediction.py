import joblib
import pandas as pd

# ---------------------------------
# Load Trained Model
# ---------------------------------

model = joblib.load(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\models\hr_attrition_model.pkl"
)

print("Model Loaded Successfully!")

# ---------------------------------
# Load One Sample Record
# ---------------------------------

sample = pd.read_csv(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\X_test.csv"
).iloc[[0]]

prediction = model.predict(sample)

print("\nPrediction Result:")

if prediction[0] == 1:
    print("Employee is likely to leave the company.")
else:
    print("Employee is likely to stay with the company.")