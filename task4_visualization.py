import pandas as pd

data = {
    "title": [
        "AI is changing the world",
        "New tech startup raises funds",
        "Python vs Java debate",
        "SpaceX launches rocket",
        "Climate change concerns",
        "Stock market update",
        "New smartphone released",
        "Gaming industry boom",
        "Cybersecurity threats rising",
        "Open source trends"
    ],
    "score": [120, 300, 150, 500, 200, 250, 180, 220, 140, 160],
    "num_comments": [30, 80, 40, 150, 60, 70, 50, 65, 35, 45],
    "category": ["tech", "business", "tech", "science", "news", "business", "tech", "gaming", "tech", "tech"]
}

df = pd.DataFrame(data)

# Add Task 3 columns
avg_score = df["score"].mean()
df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > avg_score

# Save file
df.to_csv("trends_analysed.csv", index=False)

print("File created!")



import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("trends_analysed.csv")

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# ---------------------------
# Chart 1: Top 10 Stories
# ---------------------------
top10 = df.sort_values(by="score", ascending=False).head(10)

plt.figure()
plt.barh(top10["title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()
plt.savefig("outputs/chart1_top_stories.png")
plt.show()

# ---------------------------
# Chart 2: Category Count
# ---------------------------
category_counts = df["category"].value_counts()

plt.figure()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.savefig("outputs/chart2_categories.png")
plt.show()

# ---------------------------
# Chart 3: Scatter Plot
# ---------------------------
plt.figure()

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.show()