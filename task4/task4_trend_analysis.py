import pandas as pd
import matplotlib.pyplot as plt
import os

print("Auspify Task 4 Started")

# Load cleaned dataset
df = pd.read_csv("Data/cleaned/netflix_cleaned.csv")

print("Dataset Shape:")
print(df.shape)

# Calculate yearly content releases
yearly_content = df["release_year"].value_counts().sort_index()

print("\nYearly Content Releases:")
print(yearly_content)

# Identify peak release year
peak_year = yearly_content.idxmax()
peak_count = yearly_content.max()

print("\nKey Business Insights:")
print(f"1. The peak content release year is {peak_year}.")
print(f"2. The highest number of titles released in a year is {peak_count}.")

# Create output folder
os.makedirs("task4/screenshots", exist_ok=True)

# Create trend visualization
plt.figure(figsize=(10, 6))
yearly_content.plot(kind="line", marker="o")

plt.title("Netflix Content Releases by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()

# Save chart
plt.savefig("task4/screenshots/task4_release_year_trend.png")

print("\nTask 4 visualization saved successfully!")
print("\nTask 4 analysis completed successfully!")