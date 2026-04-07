import pandas as pd

data = {
    "title": ["Story A", "Story B", "Story C"],
    "score": [100, 200, 50],
    "num_comments": [10, 40, 5],
    "category": ["tech", "news", "tech"]
}

df = pd.DataFrame(data)

df.to_csv("trends_clean.csv", index=False)


import pandas as pd
import numpy as np

# 1 — Load Data
df = pd.read_csv("data/trends_clean.csv")

# First 5 rows
print("First 5 rows:")
print(df.head())

# Shape
print("\nShape of DataFrame:", df.shape)

# Averages
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage Score:", avg_score)
print("Average Comments:", avg_comments)


# 2 — NumPy Analysis

scores = df["score"].values

print("\nMean Score:", np.mean(scores))
print("Median Score:", np.median(scores))
print("Standard Deviation:", np.std(scores))

print("\nHighest Score:", np.max(scores))
print("Lowest Score:", np.min(scores))

# Category with most stories
most_common_category = df["category"].value_counts().idxmax()
print("\nCategory with most stories:", most_common_category)

# Story with most comments
max_comments_row = df.loc[df["num_comments"].idxmax()]
print("\nStory with most comments:")
print("Title:", max_comments_row["title"])
print("Comments:", max_comments_row["num_comments"])


# 3 — Add New Columns

# Engagement
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Is Popular
df["is_popular"] = df["score"] > avg_score


# 4 — Save Result
df.to_csv("data/trends_analysed.csv", index=False)

print("\nFile saved successfully as trends_analysed.csv")