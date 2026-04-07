
import json

sample_data = [
    {"post_id": 1, "title": " AI is growing ", "score": 10, "num_comments": 5, "category": "technology"},
    {"post_id": 2, "title": "Sports News", "score": 3, "num_comments": 2, "category": "sports"},
    {"post_id": 3, "title": "Science Update", "score": 15, "num_comments": 8, "category": "science"},
    {"post_id": 1, "title": " AI is growing ", "score": 10, "num_comments": 5, "category": "technology"}
]

with open("trends_sample.json", "w") as f:
    json.dump(sample_data, f)

print("Sample JSON file created!")






import pandas as pd

# 1 — Load JSON file
file_path = "data/trends_YYYYMMDD.json"  # change filename

df = pd.read_json(file_path)

print(f"Loaded {len(df)} stories from {file_path}")

# 2 — Clean the Data

# Remove duplicates
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Drop missing values
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Fix data types
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce")

# Drop rows where conversion failed
df = df.dropna(subset=["score", "num_comments"])

# Convert to integer
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low-quality stories (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Strip whitespace from title
df["title"] = df["title"].str.strip()

# 3 — Save as CSV
output_path = "data/trends_clean.csv"
df.to_csv(output_path, index=False)

print(f"\nSaved {len(df)} rows to {output_path}")

# Category summary
print("\nStories per category:")
print(df["category"].value_counts())