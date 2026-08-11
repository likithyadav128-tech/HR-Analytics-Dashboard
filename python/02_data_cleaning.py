import pandas as pd

# ---------------------------------
# Load Dataset
# ---------------------------------

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\WA_Fn-UseC_-HR-Employee-Attrition.csv")

print("Dataset Loaded Successfully!\n")

# ---------------------------------
# Dataset Information
# ---------------------------------

print("Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# ---------------------------------
# Remove Duplicate Rows
# ---------------------------------

df = df.drop_duplicates()

print("\nShape After Removing Duplicates:", df.shape)

# ---------------------------------
# Standardize Column Names
# ---------------------------------

df.columns = df.columns.str.strip()

# ---------------------------------
# Convert Object Columns
# ---------------------------------

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype(str)

# ---------------------------------
# Save Cleaned Dataset
# ---------------------------------

save_path = r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\cleaned_hr_data.csv"

df.to_csv(save_path, index=False)

print("\nCleaned dataset saved successfully!")
print("Location:", save_path)

print("\nData Cleaning Completed Successfully!")