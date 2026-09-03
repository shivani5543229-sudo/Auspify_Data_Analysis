import pandas as pd
import matplotlib.pyplot as plt
import os

print("Auspify Task 3 Started")

# Load cleaned dataset
df = pd.read_csv("Data/cleaned/netflix_cleaned.csv")

print("Dataset Shape:")
print(df.shape)

# Extract country information
country_data = df[["show_id", "country"]].dropna()

# Split multiple countries and create separate rows
country_data["country"] = country_data["country"].str.split(", ")

country_data = country_data.explode("country")

# Count content by country
country_counts = country_data["country"].value_counts()

print("\nTop 10 Content-Producing Countries:")
print(country_counts.head(10))

# Create output folder
os.makedirs("task3/screenshots", exist_ok=True)

# Create chart
top_10 = country_counts.head(10)

plt.figure(figsize=(10, 6))
top_10.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()

# Save chart
plt.savefig("task3/screenshots/task3_country_distribution.png")

print("\nTask 3 visualization saved successfully!")

# Business insights
print("\nKey Business Insights:")
print(f"1. The top content-producing country is {country_counts.index[0]}.")
print(f"2. The top country has {country_counts.iloc[0]} titles.")
print(f"3. The top 10 countries together account for {country_counts.head(10).sum()} country-title entries.")

print("\nTask 3 analysis completed successfully!")