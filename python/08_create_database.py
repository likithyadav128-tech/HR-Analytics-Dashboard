import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\cleaned_hr_data.csv")

# Create SQLite database
conn = sqlite3.connect(r"C:\Users\likit\OneDrive\Documents\HR-Analytics-Dashboard\data\hr_analytics.db")

# Save data to table
df.to_sql("employees", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("Database created successfully!")