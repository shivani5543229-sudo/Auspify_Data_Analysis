import pandas as pd
import matplotlib.pyplot as plt

print("Auspify Task 2 Started")

# Load cleaned dataset
df = pd.read_csv("Data/cleaned/netflix_cleaned.csv")

# Display basic information
print("Dataset Shape:")
print(df.shape)

print("Content Type Count:")
content_count = df["type"].value_counts()
print(content_count)

# Calculate proportions
content_proportion = df["type"].value_counts(normalize=True) * 100

print("Content Type Proportion:")
print(content_proportion)

# Create visualization
plt.figure(figsize=(8, 5))
content_count.plot(kind="bar")

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.xticks(rotation=0)

plt.tight_layout()

# Save visualization
plt.savefig("task2_content_distribution.png")

plt.show()

print("Task 2 visualization saved successfully!")