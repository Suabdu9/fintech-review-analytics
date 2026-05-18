# Fintech Review Analytics

## Project Overview

This project analyzes customer reviews from Ethiopian banking mobile applications available on the Google Play Store. The objective is to identify customer satisfaction drivers, recurring complaints, and actionable product improvement opportunities using Natural Language Processing (NLP), thematic analysis, visualization, and PostgreSQL database engineering.

The project simulates a complete end-to-end analytics pipeline involving:

1. Data Collection and Preprocessing  
2. Sentiment and Thematic Analysis  
3. PostgreSQL Database Engineering  
4. Business Insights and Recommendations  

Banks analyzed:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

# Business Objective

Mobile banking applications generate large volumes of customer feedback through app store reviews. These reviews contain valuable information about customer satisfaction, usability challenges, operational failures, and requested features.

The goal of this project is to transform unstructured customer feedback into actionable business insights that can support:

- Product improvement
- Customer experience enhancement
- Technical issue prioritization
- Feature planning
- Data-driven decision making

---

# Task 1: Data Collection and Preprocessing

## Scraping Methodology

Customer reviews were collected from the Google Play Store using:

- `google-play-scraper`

The scraping workflow was implemented in Python and designed as a reusable pipeline capable of collecting reviews from multiple banking applications.

The following fields were collected:

- Review text
- Rating (1–5)
- Review date
- Bank/application name
- Source platform

---

## Banking Applications Scraped

| Bank | App ID |
|---|---|
| Commercial Bank of Ethiopia | `com.combanketh.mobilebanking` |
| Bank of Abyssinia | `com.boa.boaMobileBanking` |
| Dashen Bank | `com.dashen.dashensuperapp` |

---

## Data Preprocessing

The preprocessing pipeline included:

1. Removing duplicate reviews using review identifiers  
2. Dropping rows with missing review text or ratings  
3. Normalizing review dates into `YYYY-MM-DD` format  
4. Lowercasing review text  
5. Tokenization  
6. Stop-word removal  
7. Lemmatization using spaCy  

Final cleaned dataset columns:

- `review`
- `rating`
- `date`
- `bank`
- `source`

---

## Data Quality Summary

Project targets:
- Minimum 400 reviews per bank
- Minimum 1,200 total reviews

Data quality improvements included:
- Duplicate removal
- Missing-value handling
- Standardized formatting
- Structured export formatting

Missing-value presence remained below 5% after preprocessing.

---

# Task 2: Sentiment and Thematic Analysis

## Sentiment Analysis

Sentiment analysis was implemented using:

- `distilbert-base-uncased-finetuned-sst-2-english`

The transformer model classified reviews into:
- Positive
- Neutral
- Negative

Each review received:
- A sentiment label
- A confidence score

Additionally, VADER sentiment analysis was implemented as a lightweight baseline comparison approach.

---

## NLP Pipeline

The NLP preprocessing workflow included:

- Lowercasing
- Tokenization
- Stop-word removal
- Lemmatization

Reusable modular functions were implemented to improve:
- Maintainability
- Reusability
- Scalability

Basic error handling was added for:
- Dataset loading
- Model inference
- CSV export
- Database insertion

---

## Thematic Analysis

TF-IDF keyword extraction and n-gram analysis were used to identify recurring business-related themes.

Common extracted keywords included:
- "login error"
- "otp issue"
- "slow transfer"
- "app crash"
- "fingerprint login"

Themes identified included:
- Account Access Issues
- Transaction Performance
- App Stability
- UI & UX
- Feature Requests

---

## Visualizations

The project includes visualizations such as:
- Sentiment distribution by bank
- Rating distribution per bank
- Theme frequency analysis
- Keyword frequency analysis
- Comparative sentiment charts

Generated visualizations are stored in:

```text
plots/
```

---

# Task 3: PostgreSQL Database Engineering

## Database Setup

PostgreSQL was used to store processed review data in a structured relational database.

Database created:

```text
bank_reviews
```

Python database integration was implemented using:

- `psycopg2-binary`

---

## Database Schema

Two relational tables were designed:

### Banks Table

Stores banking application metadata.

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

## Verification Queries

Verification queries were executed to validate:
- Review counts per bank
- Average ratings per bank
- Null values in critical columns

SQL files included:
- `schema.sql`
- `verification_queries.sql`

---

# Task 4: Insights and Recommendations

## Key Findings

### Commercial Bank of Ethiopia (CBE)

#### Satisfaction Drivers
- Convenient mobile transactions
- Strong customer adoption

#### Pain Points
- OTP authentication failures
- Delayed transaction confirmations

#### Recommendations
- Improve authentication reliability
- Optimize backend transaction processing

---

### Bank of Abyssinia (BOA)

#### Satisfaction Drivers
- Positive user interface feedback
- Easy navigation experience

#### Pain Points
- Application crashes
- Slow loading performance

#### Recommendations
- Improve stability testing
- Optimize performance for low-resource devices

---

### Dashen Bank

#### Satisfaction Drivers
- Feature-rich application experience
- Positive convenience feedback

#### Pain Points
- Login session instability
- Customer feature requests

#### Recommendations
- Improve session management reliability
- Prioritize requested features

---

# Comparative Insights

Across all three banking applications:

- Positive sentiment dominated overall reviews
- Authentication reliability remained a major concern
- Transaction speed strongly influenced customer satisfaction
- App stability significantly affected negative ratings

---

# Ethical Considerations

This project analyzed only publicly available Google Play reviews.

Considerations included:
- Avoiding exposure of personal information
- Using aggregated insights instead of targeting individuals
- Acknowledging potential reviewer bias
- Respecting public platform boundaries

---

# Limitations

Several limitations should be acknowledged:

- Google Play reviews may change over time
- Review availability differs across applications
- Reviews may contain sarcasm or ambiguous sentiment
- Only Android Google Play reviews were analyzed
- Theme classification partially relied on manual grouping logic

---

# Suggested Next Steps

Potential future improvements include:

- Topic modeling using LDA or NMF
- Multilingual NLP support
- Real-time dashboard deployment
- Automated ETL workflows
- Comparative benchmarking with international banking applications

---

# Output Directories

The project generates outputs in the following directories:

- `data/raw/`
  Stores scraped review datasets

- `data/processed/`
  Stores cleaned and analyzed datasets

- `plots/`
  Stores generated visualizations

- `notebooks/`
  Stores exploratory and analytical notebooks

- `sql/`
  Stores PostgreSQL schema and verification queries

- `database/`
  Stores PostgreSQL insertion scripts

---
# Installation and Setup

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd fintech-review-analytics
```

---

## 2. Create and Activate Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Reproducing the Project

## Step 1: Run Review Scraping

```bash
python scripts/scrape_reviews.py
```

This collects Google Play reviews for:
- Commercial Bank of Ethiopia
- Bank of Abyssinia
- Dashen Bank

Raw review datasets are saved in:

```text
data/raw/
```

---

## Step 2: Run Sentiment and Thematic Analysis

Open and run:

```text
notebooks/sentiment_analysis.ipynb
```

OR run the analysis script if available:

```bash
python scripts/sentiment_analysis.py
```

This performs:
- NLP preprocessing
- sentiment analysis
- TF-IDF keyword extraction
- thematic analysis

Processed datasets are saved in:

```text
data/processed/
```

Generated plots are saved in:

```text
plots/
```

---

## Step 3: Configure PostgreSQL

Install PostgreSQL and create the database:

```text
bank_reviews
```

Then execute:

```text
sql/schema.sql
```

to create the required tables.

---

## Step 4: Load Data into PostgreSQL

Run:

```bash
python database/load_to_postgres.py
```

This inserts processed review data into PostgreSQL.

---

## Step 5: Run Verification Queries

Execute:

```text
sql/verification_queries.sql
```

to validate:
- review counts
- average ratings
- null-value checks

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
- Git
- GitHub Actions

---

# Repository Workflow

The project followed a task-based Git workflow:

- `task-1` → Data Collection and Preprocessing
- `task-2` → Sentiment and Thematic Analysis
- `task-3` → PostgreSQL Database Engineering
- `task-4` → Insights and Recommendations

All tasks were merged into the `main` branch using Pull Requests.