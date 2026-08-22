import pandas as pd

print("Auspify Task 1 Started")

df = pd.read_csv("Data/netflix_titles.csv")

print(df.head())
print("Dataset Shape:")
print(df.shape)
print("Column Names:")
print(df.columns.tolist())
print("Data Types:")
print(df.dtypes)
print("Missing Values:")
print(df.isnull().sum())
print("Duplicate Rows:")
print(df.duplicated().sum())
print("Date Added Sample:")
print(df["date_added"].head(10))
df["date_added"] = pd.to_datetime(df["date_added"])

print("Date Added Data Type:")
print(df["date_added"].dtype)

# Clean duration
df["duration_value"] = df["duration"].str.extract(r"(\d+)").astype(int)

print("Duration Sample:")
print(df[["duration", "duration_value"]].head(10))

# Extract duration unit
df["duration_unit"] = df["duration"].str.extract(r"(min|Season|Seasons)")

# Standardize unit names
df["duration_unit"] = df["duration_unit"].replace({
    "min": "Minutes",
    "Season": "Seasons"
})

print("Cleaned Duration:")
print(df[["duration", "duration_value", "duration_unit"]].head(10))
print("Rating Values:")
print(df["rating"].value_counts())
print("Content Type Values:")
print(df["type"].value_counts())
print("Country Sample:")
print(df["country"].head(10))

print("Unique Country Values:")
print(df["country"].nunique())

print("Final Missing Values:")
print(df.isnull().sum())

print("Final Missing Values:")
print(df.isnull().sum())

print("Final Duplicate Rows:")
print(df.duplicated().sum())

import os

output_path = "data/cleaned/netflix_cleaned.csv"

os.makedirs("data/cleaned", exist_ok=True)

df.to_csv(output_path, index=False)

print("Cleaned dataset saved successfully!")
print("File:", output_path)