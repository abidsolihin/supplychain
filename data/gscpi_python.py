import pandas as pd

# Load dataset, forcing first row to be treated as data
file_path = "C:/Users/Abid/Desktop/gscpi_data.xlsx"
df = pd.read_excel(file_path, engine="openpyxl", header=None)  # No header row

# Rename the first two columns correctly
df = df.iloc[:, :2]  # Keep only first 2 columns
df.columns = ["Date", "GSCPI"]

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Remove invalid dates
df = df.dropna(subset=["Date"])

# Sort data
df = df.sort_values(by="Date")

# Save cleaned data
df.to_csv("C:/Users/Abid/Desktop/gscpi_cleaned.csv", index=False)

print("✅ Data cleaned and saved successfully!")
