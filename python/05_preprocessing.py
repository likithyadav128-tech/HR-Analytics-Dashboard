import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# ----------------------------------
# Load Cleaned Dataset
# ----------------------------------

df = pd.read_csv(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\cleaned_hr_data.csv"
)

print("Dataset Loaded Successfully!")

# ----------------------------------
# Encode Categorical Columns
# ----------------------------------

encoder = LabelEncoder()

for col in df.select_dtypes(include="object").columns:
    df[col] = encoder.fit_transform(df[col])

print("Categorical Columns Encoded Successfully!")

# ----------------------------------
# Separate Features and Target
# ----------------------------------

X = df.drop("Attrition", axis=1)
y = df["Attrition"]

print("\nFeature Shape :", X.shape)
print("Target Shape :", y.shape)

# ----------------------------------
# Split Dataset
# ----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Shape :", X_train.shape)
print("Testing Shape :", X_test.shape)

# ----------------------------------
# Save Processed Dataset
# ----------------------------------

X_train.to_csv(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\X_train.csv",
    index=False
)

X_test.to_csv(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\X_test.csv",
    index=False
)

y_train.to_csv(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\y_train.csv",
    index=False
)

y_test.to_csv(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\y_test.csv",
    index=False
)

print("\nProcessed datasets saved successfully!")
print("\nPreprocessing Completed Successfully!")