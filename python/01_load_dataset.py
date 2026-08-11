import pandas as pd

# ---------------------------------
# Load Dataset
# ---------------------------------

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\WA_Fn-UseC_-HR-Employee-Attrition.csv")

print("Dataset Loaded Successfully!\n")

print("Shape of Dataset:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())