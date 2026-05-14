"""
Scrape and preprocess reviews from the Google Play Store for the specified bank apps.
"""

from google_play_scraper import reviews, Sort
import pandas as pd
import os

# Bank application IDs on the Google Play Store

BANK_APPS = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}


def fetch_reviews(app_id, bank_name, count=500):
    # Fetch reviews for the specified banking app
    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        sort=Sort.NEWEST,
        count=count
    )

    data = []
    # Extract relevant information from each review

    for review in result:
        data.append({
            "review_id": review.get("reviewId"),
            "review": review.get("content"),
            "rating": review.get("score"),
            "date": review.get("at").strftime("%Y-%m-%d") if review.get("at") else None,
            "bank": bank_name,
            "source": "Google Play"
        })

    return pd.DataFrame(data)


def preprocess_reviews(df):
    # Clean the scraped reviews by removing duplicates and handling missing values

    initial_count = len(df)

    # Remove duplicate reviews
    df = df.drop_duplicates(subset=["review_id"])

    # Remove rows with missing review or rating
    df = df.dropna(subset=["review", "rating"])

    final_count = len(df)

    print(f"Initial reviews: {initial_count}")
    print(f"Cleaned reviews: {final_count}")
    print(f"Removed reviews: {initial_count - final_count}")

    return df


def main():
    # Run the scraping and preprocessing pipeline for all specified bank apps

    all_reviews = []

    for bank_name, app_id in BANK_APPS.items():
        print(f"\nScraping reviews for {bank_name}...")

        df = fetch_reviews(app_id, bank_name)

        print(f"Collected {len(df)} reviews.")

        cleaned_df = preprocess_reviews(df)

        all_reviews.append(cleaned_df)

    #combine all bank reviews datasets
    final_df = pd.concat(all_reviews, ignore_index=True)

    # Keep only the relevant columns for the final dataset
    final_df = final_df[
        ["review", "rating", "date", "bank", "source"]
    ]

    # Create output directory if it doesn't exist
    os.makedirs("data/raw", exist_ok=True)

    # Save the cleaned dataset to a CSV file
    final_df.to_csv(
        "data/raw/bank_reviews.csv",
        index=False
    )

    print("\nDataset saved successfully.")
    print(final_df.head())


if __name__ == "__main__":
    main()