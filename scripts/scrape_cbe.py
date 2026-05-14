from google_play_scraper import reviews, Sort
import pandas as pd


APP_ID = "com.combanketh.mobilebanking"
BANK_NAME = "Commercial Bank of Ethiopia"


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

    # Remove duplicates
    df = df.drop_duplicates(subset=["review_id"])

    # Drop missing values
    df = df.dropna(subset=["review", "rating"])

    final_count = len(df)

    print(f"Initial reviews: {initial_count}")
    print(f"Cleaned reviews: {final_count}")
    print(f"Removed reviews: {initial_count - final_count}")

    return df


def main():
    df = fetch_reviews(APP_ID, BANK_NAME)

    cleaned_df = preprocess_reviews(df)

    cleaned_df = cleaned_df[
        ["review", "rating", "date", "bank", "source"]
    ]

    cleaned_df.to_csv(
        "data/raw/cbe_reviews.csv",
        index=False
    )

    print(cleaned_df.head())
    print("CBE reviews saved successfully.")


if __name__ == "__main__":
    main()