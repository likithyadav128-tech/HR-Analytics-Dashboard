import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Cleaned Dataset
# -----------------------------

df = pd.read_csv(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\cleaned_hr_data.csv"
)

print("Dataset Loaded Successfully!")
print(df.head())

# -----------------------------
# Dataset Information
# -----------------------------

print("\nDataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())

# -----------------------------
# Employee Attrition Count
# -----------------------------

plt.figure(figsize=(5,4))
sns.countplot(x="Attrition", data=df)
plt.title("Employee Attrition")
plt.show()

# -----------------------------
# Gender Distribution
# -----------------------------

plt.figure(figsize=(5,4))
sns.countplot(x="Gender", data=df)
plt.title("Gender Distribution")
plt.show()

# -----------------------------
# Department Distribution
# -----------------------------

plt.figure(figsize=(6,4))
sns.countplot(y="Department", data=df)
plt.title("Department Distribution")
plt.show()

# -----------------------------
# Job Role Distribution
# -----------------------------

plt.figure(figsize=(8,5))
sns.countplot(y="JobRole", data=df)
plt.title("Job Role Distribution")
plt.show()

# -----------------------------
# Monthly Income Distribution
# -----------------------------

plt.figure(figsize=(6,4))
plt.hist(df["MonthlyIncome"], bins=20)
plt.title("Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Employees")
plt.show()

# -----------------------------
# Age Distribution
# -----------------------------

plt.figure(figsize=(6,4))
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Employees")
plt.show()

# -----------------------------
# Correlation Heatmap
# -----------------------------

plt.figure(figsize=(12,8))

corr = df.select_dtypes(include="number").corr()

sns.heatmap(corr, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

print("\nEDA Completed Successfully!")