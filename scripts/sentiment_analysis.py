"""
Sentiment and thematic analysis pipeline
for Ethiopian banking app reviews.
"""

import pandas as pd
import spacy

from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load DistilBERT sentiment model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Initialize VADER
vader = SentimentIntensityAnalyzer()


def preprocess_text(text):
    """
    Preprocess review text using:
    - tokenization
    - stop-word removal
    - lemmatization
    """

    doc = nlp(str(text).lower())

    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop
        and not token.is_punct
        and token.is_alpha
    ]

    return " ".join(tokens)


def distilbert_sentiment(text):
    """
    Predict sentiment using DistilBERT.
    """

    result = sentiment_pipeline(text[:512])[0]

    label = result["label"]
    score = result["score"]

    if score < 0.60:
        sentiment = "neutral"

    elif label == "POSITIVE":
        sentiment = "positive"

    else:
        sentiment = "negative"

    return sentiment, score


def vader_sentiment(text):
    """
    Predict sentiment using VADER.
    """

    score = vader.polarity_scores(str(text))

    compound = score["compound"]

    if compound >= 0.05:
        label = "positive"

    elif compound <= -0.05:
        label = "negative"

    else:
        label = "neutral"

    return label, compound


def assign_theme(text):
    """
    Assign business-related themes.
    """

    text = str(text).lower()

    # Account access issues
    if any(word in text for word in [
        "login",
        "password",
        "otp",
        "account",
        "sign in"
    ]):
        return "Account Access Issues"

    # Transaction performance
    elif any(word in text for word in [
        "slow",
        "transfer",
        "transaction",
        "payment",
        "delay"
    ]):
        return "Transaction Performance"

    # App stability
    elif any(word in text for word in [
        "crash",
        "freeze",
        "bug",
        "error",
        "stuck"
    ]):
        return "App Stability"

    # UI & UX
    elif any(word in text for word in [
        "ui",
        "ux",
        "design",
        "interface",
        "navigation"
    ]):
        return "UI & UX"

    # Feature requests
    elif any(word in text for word in [
        "feature",
        "fingerprint",
        "update",
        "notification",
        "dark mode"
    ]):
        return "Feature Requests"

    return "Other"


def extract_keywords(texts, top_n=20):
    """
    Extract keywords and n-grams using TF-IDF.
    """

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 3),
        max_features=top_n
    )

    tfidf_matrix = vectorizer.fit_transform(texts)

    return vectorizer.get_feature_names_out()


def main():

    # Load cleaned Task 1 dataset
    df = pd.read_csv("data/raw/bank_reviews.csv")

    # Create review IDs
    df["review_id"] = range(1, len(df) + 1)

    # Preprocess reviews
    df["cleaned_review"] = df["review"].apply(preprocess_text)

    # DistilBERT sentiment analysis
    distilbert_results = df["review"].apply(
        distilbert_sentiment
    )

    df["sentiment_label"] = distilbert_results.apply(
        lambda x: x[0]
    )

    df["sentiment_score"] = distilbert_results.apply(
        lambda x: x[1]
    )

    # VADER sentiment analysis
    vader_results = df["review"].apply(
        vader_sentiment
    )

    df["vader_label"] = vader_results.apply(
        lambda x: x[0]
    )

    df["vader_score"] = vader_results.apply(
        lambda x: x[1]
    )

    # Assign themes
    df["identified_theme"] = df["review"].apply(
        assign_theme
    )

    # Extract keywords per bank
    for bank in df["bank"].unique():

        print(f"\nTop keywords for {bank}")

        bank_reviews = df[
            df["bank"] == bank
        ]

        keywords = extract_keywords(
            bank_reviews["cleaned_review"]
        )

        print(keywords)

    # Sentiment aggregation by bank
    bank_sentiment = (
        df.groupby("bank")["sentiment_score"]
        .mean()
        .reset_index()
    )

    print("\nAverage sentiment by bank:")
    print(bank_sentiment)

    # Sentiment aggregation by rating
    rating_sentiment = (
        df.groupby("rating")["sentiment_score"]
        .mean()
        .reset_index()
    )

    print("\nAverage sentiment by rating:")
    print(rating_sentiment)

    # Theme distribution per bank
    theme_summary = (
        df.groupby(["bank", "identified_theme"])
        .size()
        .reset_index(name="count")
    )

    print("\nTheme distribution per bank:")
    print(theme_summary)

    # Save analyzed dataset
    output_df = df[
        [
            "review_id",
            "review",
            "bank",
            "rating",
            "sentiment_label",
            "sentiment_score",
            "identified_theme"
        ]
    ]

    output_df = output_df.rename(
        columns={"review": "review_text"}
    )

    output_df.to_csv(
        "data/processed/analyzed_bank_reviews.csv",
        index=False
    )

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()