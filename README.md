# Fintech Review Analytics

## Project Overview

This project analyzes customer reviews from Ethiopian banking mobile applications available on the Google Play Store. The goal is to identify customer satisfaction drivers, recurring complaints, and actionable product improvement opportunities using Natural Language Processing (NLP), thematic analysis, and PostgreSQL database engineering.

The project follows a four-stage analytics pipeline:

1. Data Collection and Preprocessing
2. Sentiment and Thematic Analysis
3. PostgreSQL Database Engineering
4. Insights and Recommendations

Banks analyzed:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

# Task 1: Data Collection and Preprocessing

## Scraping Methodology

User reviews were scraped from the Google Play Store using the Python library:

- `google-play-scraper`

The scraping pipeline was implemented in Python and designed as a reusable workflow capable of processing multiple banking applications in a single execution.

The following information was collected for each review:

- Review text
- Rating (1–5)
- Review date
- Bank/app name
- Review source

---

## Apps Scraped

| Bank | App ID |
|------|------|
| Commercial Bank of Ethiopia | `com.combanketh.mobilebanking` |
| Bank of Abyssinia | `com.boa.boaMobileBanking` |
| Dashen Bank | `com.dashen.dashensuperapp` |

---

## Data Preprocessing Steps

The preprocessing pipeline included:

1. Removing duplicate reviews using review IDs
2. Dropping rows with missing review text or ratings
3. Normalizing review dates to `YYYY-MM-DD`
4. Text preprocessing using:
   - Tokenization
   - Stop-word removal
   - Lemmatization with spaCy
5. Exporting cleaned datasets into CSV format

Final cleaned dataset columns:

- `review`
- `rating`
- `date`
- `bank`
- `source`

---

## Data Quality Summary

- Target: 400+ reviews per bank
- Total target: 1,200+ reviews
- Missing values were removed during preprocessing
- Duplicate reviews were removed before export
- Final dataset achieved low missing-value presence and standardized formatting

---

## Limitations

- Google Play reviews may change over time as users edit or delete reviews
- Some apps may provide fewer reviews depending on availability and scraper limitations
- Only publicly available Google Play reviews were analyzed

---

# Task 2: Sentiment and Thematic Analysis

## Sentiment Analysis

Sentiment analysis was performed using the transformer model:

- `distilbert-base-uncased-finetuned-sst-2-english`

The model classified reviews into:
- Positive
- Neutral
- Negative

Each review was assigned a confidence score.

Additionally, VADER sentiment analysis was implemented as a lexicon-based baseline model for comparison purposes.

---

## NLP Preprocessing Pipeline

The NLP preprocessing pipeline included:

- Lowercasing
- Tokenization
- Stop-word removal
- Lemmatization using spaCy

Reusable and modular functions were implemented to improve maintainability and reproducibility.

Basic error handling was added for:
- Dataset loading
- Model initialization
- Sentiment prediction
- CSV export operations

---

## Thematic Analysis

TF-IDF keyword extraction and n-gram analysis were used to identify recurring business-related themes across customer reviews.

Themes identified included:

- Account Access Issues
- Transaction Performance
- App Stability
- UI & UX
- Feature Requests

Example recurring keywords included:
- "login error"
- "otp issue"
- "slow transfer"
- "app crash"
- "fingerprint login"

---

## Visualizations

The project includes visualizations such as:

- Sentiment distribution by bank
- Average sentiment score by rating
- Theme distribution per bank
- Word cloud analysis

Visualizations were implemented directly in Jupyter notebooks using:
- Matplotlib
- Seaborn

---

## Analyzed Dataset

The processed analytical dataset includes:

- `review_id`
- `review_text`
- `bank`
- `rating`
- `sentiment_label`
- `sentiment_score`
- `identified_theme`

The analyzed dataset was exported to:

```text
data/processed/analyzed_bank_reviews.csv
```

---

# Task 3: PostgreSQL Database Engineering

## Database Setup

PostgreSQL was used to store cleaned and processed banking review data in a relational database format.

Database created:

```text
bank_reviews
```

Python database connectivity was implemented using:

- `psycopg2-binary`

---

## Database Schema

Two relational tables were designed:

### Banks Table

Stores metadata about banking applications.

Columns:
- `bank_id`
- `bank_name`
- `app_name`

### Reviews Table

Stores processed review data and analytical outputs.

Columns:
- `review_id`
- `bank_id`
- `review_text`
- `rating`
- `review_date`
- `sentiment_label`
- `sentiment_score`
- `identified_theme`
- `source`

---

## Data Insertion Pipeline

A Python insertion pipeline was implemented to:

- Load processed review datasets
- Insert bank metadata
- Insert processed review records into PostgreSQL tables

The insertion workflow was implemented using:

```text
database/load_to_postgres.py
```

---

## Verification Queries

SQL verification queries were executed to validate:

- Total reviews per bank
- Average rating per bank
- Null values in critical columns

Verification queries are located in:

```text
sql/verification_queries.sql
```

---

# Output Directories

The project generates outputs in the following directories:

- `data/raw/`
  Stores scraped review datasets.

- `data/processed/`
  Stores cleaned and analyzed datasets.

- `plots/`
  Stores generated visualizations and exported figures.

- `notebooks/`
  Stores exploratory and analytical Jupyter notebooks.

- `sql/`
  Stores PostgreSQL schema and verification queries.

- `database/`
  Stores PostgreSQL insertion scripts.

---

# Project Structure

```text
fintech-review-analytics/
├── .github/workflows/
├── data/
│   ├── raw/
│   └── processed/
├── database/
├── notebooks/
├── plots/
├── scripts/
├── sql/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Technologies Used

- Python
- Pandas
- spaCy
- Transformers
- VADER
- Scikit-learn
- Matplotlib
- Seaborn
- PostgreSQL
- psycopg2
- Git & GitHub Actions

---

# Future Improvements

Potential future improvements include:

- Advanced dashboard visualizations
- Additional comparative banking analytics
- More advanced theme classification techniques