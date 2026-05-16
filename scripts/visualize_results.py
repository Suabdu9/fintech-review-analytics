"""
Visualization script for
bank review sentiment analysis.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from wordcloud import WordCloud


# Create plots directory
os.makedirs("plots", exist_ok=True)

# Load analyzed dataset
df = pd.read_csv(
    "data/processed/analyzed_bank_reviews.csv"
)


# -----------------------------------
# 1. Sentiment Distribution by Bank
# -----------------------------------

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="bank",
    hue="sentiment_label"
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")

plt.xticks(rotation=10)

plt.tight_layout()

plt.savefig(
    "plots/sentiment_distribution_by_bank.png"
)

plt.close()


# -----------------------------------
# 2. Average Sentiment Score by Bank
# -----------------------------------

bank_sentiment = (
    df.groupby("bank")["sentiment_score"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(8, 5))

sns.barplot(
    data=bank_sentiment,
    x="bank",
    y="sentiment_score"
)

plt.title("Average Sentiment Score by Bank")
plt.xlabel("Bank")
plt.ylabel("Average Sentiment Score")

plt.tight_layout()

plt.savefig(
    "plots/average_sentiment_by_bank.png"
)

plt.close()


# -----------------------------------
# 3. Theme Distribution
# -----------------------------------

plt.figure(figsize=(10, 6))

theme_counts = (
    df["identified_theme"]
    .value_counts()
)

sns.barplot(
    x=theme_counts.values,
    y=theme_counts.index
)

plt.title("Theme Frequency Distribution")
plt.xlabel("Frequency")
plt.ylabel("Theme")

plt.tight_layout()

plt.savefig(
    "plots/theme_distribution.png"
)

plt.close()


# -----------------------------------
# 4. Rating Distribution by Bank
# -----------------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="bank",
    y="rating"
)

plt.title("Rating Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Rating")

plt.tight_layout()

plt.savefig(
    "plots/rating_distribution_by_bank.png"
)

plt.close()


# -----------------------------------
# 5. Word Cloud
# -----------------------------------

text = " ".join(
    df["review_text"].astype(str)
)

wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color="white"
).generate(text)

plt.figure(figsize=(12, 6))

plt.imshow(wordcloud)

plt.axis("off")

plt.title("Common Words in Reviews")

plt.tight_layout()

plt.savefig(
    "plots/review_wordcloud.png"
)

plt.close()


# -----------------------------------
# 6. Theme Distribution Per Bank
# -----------------------------------

theme_bank = (
    df.groupby(["bank", "identified_theme"])
    .size()
    .reset_index(name="count")
)

plt.figure(figsize=(12, 6))

sns.barplot(
    data=theme_bank,
    x="bank",
    y="count",
    hue="identified_theme"
)

plt.title("Theme Distribution Per Bank")
plt.xlabel("Bank")
plt.ylabel("Theme Count")

plt.tight_layout()

plt.savefig(
    "plots/theme_distribution_per_bank.png"
)

plt.close()


print("All visualizations generated successfully.")