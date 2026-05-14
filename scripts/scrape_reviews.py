from google_play_scraper import reviews, Sort
import pandas as pd
import os


BANK_APPS = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}


def fetch_reviews(app_id, bank_name, count=500):
    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        sort=Sort.NEWEST,
        count=count
    )

    data = []

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
    all_reviews = []

    for bank_name, app_id in BANK_APPS.items():
        print(f"\nScraping reviews for {bank_name}...")

        df = fetch_reviews(app_id, bank_name)

        print(f"Collected {len(df)} reviews.")

        cleaned_df = preprocess_reviews(df)

        all_reviews.append(cleaned_df)

    final_df = pd.concat(all_reviews, ignore_index=True)

    final_df = final_df[
        ["review", "rating", "date", "bank", "source"]
    ]

    os.makedirs("data/raw", exist_ok=True)

    final_df.to_csv(
        "data/raw/bank_reviews.csv",
        index=False
    )

    print("\nDataset saved successfully.")
    print(final_df.head())


if __name__ == "__main__":
    main()