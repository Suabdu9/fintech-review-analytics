import pandas as pd
import psycopg2


# Database connection

conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user="postgres",
    password="Sumi@8900"
)

cur = conn.cursor()


# Load analyzed dataset

df = pd.read_csv(
    "data/processed/analyzed_bank_reviews.csv"
)


# Insert banks

banks = [
    (
        "Commercial Bank of Ethiopia",
        "CBE"
    ),
    (
        "Bank of Abyssinia",
        "BOA"
    ),
    (
        "Dashen Bank",
        "Dashen"
    )
]

for bank_name, app_name in banks:

    cur.execute(
        """
        INSERT INTO banks (
            bank_name,
            app_name
        )
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING;
        """,
        (bank_name, app_name)
    )


conn.commit()


# Get bank IDs

cur.execute(
    """
    SELECT bank_id, bank_name
    FROM banks;
    """
)

bank_mapping = {
    name: bank_id
    for bank_id, name in cur.fetchall()
}


# Insert reviews

for _, row in df.iterrows():

    bank_id = bank_mapping.get(
        row["bank"]
    )

    cur.execute(
        """
        INSERT INTO reviews (

            bank_id,
            review_text,
            rating,
            review_date,
            sentiment_label,
            sentiment_score,
            identified_theme,
            source

        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """,
        (
            bank_id,
            row["review_text"],
            row["rating"],
            row.get("date"),
            row["sentiment_label"],
            row["sentiment_score"],
            row["identified_theme"],
            "Google Play"
        )
    )


conn.commit()

print("Data inserted successfully.")


cur.close()
conn.close()