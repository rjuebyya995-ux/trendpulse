import pandas as pd

data = {
    "title": [
        "AI is changing the world",
        "Startup raises millions",
        "Python vs Java debate",
        "SpaceX launches rocket",
        "Climate change concerns",
        "Stock market update",
        "New smartphone released",
        "Gaming industry boom",
        "Cybersecurity threats",
        "Open source trends"
    ],
    "score": [120, 300, 150, 500, 200, 250, 180, 220, 140, 160],
    "num_comments": [30, 80, 40, 150, 60, 70, 50, 65, 35, 45],
    "category": ["tech", "business", "tech", "science", "news", "business", "tech", "gaming", "tech", "tech"]
}

df = pd.DataFrame(data)

# Save raw file (Task 1 style)
df.to_csv("trends_raw.csv", index=False)

print("Task 1 file created: trends_raw.csv")



all_posts = []

for story_id in story_ids:
    try:
        r = requests.get(ITEM_URL.format(story_id), headers=headers)
        data = r.json()

        if not data:
            continue

        title = data.get("title", "").lower()

        category = None

        for cat in categories:
            for word in categories[cat]:
                if word in title:
                    category = cat
                    break

        if category is None:
            continue

        post = {
            "post_id": data.get("id"),
            "title": data.get("title"),
            "subreddit": category,
            "score": data.get("score", 0),
            "num_comments": data.get("descendants", 0),
            "author": data.get("by")
        }

        all_posts.append(post)

    except:
        print("error with id:", story_id)




    import requests
import time
import json
import os
from datetime import datetime

# urls for hackernews api
top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# adding header (important)
headers = {"User-Agent": "TrendPulse/1.0"}

# categories + keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# storing category-wise data
data_by_category = {}
for cat in categories:
    data_by_category[cat] = []

print("starting to fetch top stories...")

# step 1: get ids
try:
    res = requests.get(top_url, headers=headers)
    story_ids = res.json()[:500]
except:
    print("error fetching top stories")
    story_ids = []

# step 2: fetch each story
for sid in story_ids:
    try:
        r = requests.get(item_url.format(sid), headers=headers)
        story = r.json()

        if not story or "title" not in story:
            continue

        title = story.get("title", "").lower()

        # find category
        found_category = None

        for cat in categories:
            for word in categories[cat]:
                if word in title:
                    found_category = cat
                    break
            if found_category:
                break

        # skip if no category
        if not found_category:
            continue

        # limit 25 per category
        if len(data_by_category[found_category]) >= 25:
            continue

        # create post object
        post = {
            "post_id": story.get("id"),
            "title": story.get("title"),
            "subreddit": found_category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by")
        }

        data_by_category[found_category].append(post)

    except:
        print("error on id:", sid)

    # stop if all full
    done = True
    for c in data_by_category:
        if len(data_by_category[c]) < 25:
            done = False
            break

    if done:
        break

# combine all data
all_posts = []
for cat in data_by_category:
    all_posts.extend(data_by_category[cat])

print("total collected:", len(all_posts))

# step 3: save json

# make folder
os.makedirs("data", exist_ok=True)

# filename with date
date_str = datetime.now().strftime("%Y%m%d")
file_name = f"data/trends_{date_str}.json"

# save
with open(file_name, "w") as f:
    json.dump(all_posts, f, indent=2)

print("saved to file:", file_name)    