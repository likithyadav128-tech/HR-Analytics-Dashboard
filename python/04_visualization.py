import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Load Cleaned Dataset
# ----------------------------

df = pd.read_csv(
    r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\cleaned_hr_data.csv"
)

print("Dataset Loaded Successfully!")

# Set Style
sns.set_style("whitegrid")

# ----------------------------
# Attrition by Department
# ----------------------------

plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Department", hue="Attrition")
plt.title("Attrition by Department")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# ----------------------------
# Attrition by Gender
# ----------------------------

plt.figure(figsize=(6,5))
sns.countplot(data=df, x="Gender", hue="Attrition")
plt.title("Attrition by Gender")
plt.tight_layout()
plt.show()

# ----------------------------
# Attrition by Job Role
# ----------------------------

plt.figure(figsize=(10,6))
sns.countplot(data=df, y="JobRole", hue="Attrition")
plt.title("Attrition by Job Role")
plt.tight_layout()
plt.show()

# ----------------------------
# Monthly Income vs Attrition
# ----------------------------

plt.figure(figsize=(8,5))
sns.boxplot(data=df, x="Attrition", y="MonthlyIncome")
plt.title("Monthly Income vs Attrition")
plt.tight_layout()
plt.show()

# ----------------------------
# Age Distribution by Attrition
# ----------------------------

plt.figure(figsize=(8,5))
sns.histplot(data=df, x="Age", hue="Attrition", bins=20)
plt.title("Age Distribution by Attrition")
plt.tight_layout()
plt.show()

# ----------------------------
# Job Satisfaction
# ----------------------------

plt.figure(figsize=(7,5))
sns.countplot(data=df, x="JobSatisfaction", hue="Attrition")
plt.title("Job Satisfaction vs Attrition")
plt.tight_layout()
plt.show()

print("\nVisualization Completed Successfully!")