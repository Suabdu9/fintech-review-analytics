# Fintech Review Analytics

## Project Overview

This project analyzes customer reviews from Ethiopian banking mobile applications on the Google Play Store. The goal is to identify customer satisfaction drivers, recurring complaints, and actionable product improvement opportunities.

Banks analyzed:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

## Task 1: Data Collection and Preprocessing

### Scraping Methodology

User reviews were scraped from the Google Play Store using the Python library:

- `google-play-scraper`

The following information was collected for each review:

- Review text
- Rating (1–5)
- Review date
- Bank/app name
- Review source

### Apps Scraped

| Bank | App ID |
|------|------|
| Commercial Bank of Ethiopia | `com.combanketh.mobilebanking` |
| Bank of Abyssinia | `com.boa.boaMobileBanking` |
| Dashen Bank | `com.dashen.dashensuperapp` |

### Data Preprocessing Steps

The preprocessing pipeline included:

1. Removing duplicate reviews using review IDs
2. Dropping rows with missing review text or ratings
3. Normalizing review dates to `YYYY-MM-DD`
4. Exporting a cleaned CSV dataset

Final dataset columns:

- `review`
- `rating`
- `date`
- `bank`
- `source`

## Output Directories

The project generates outputs in the following directories:

- data/raw/
  Stores scraped review datasets.

- data/processed/
  Stores cleaned and analyzed datasets.

- plots/
  Stores generated visualizations and exported figures.

- notebooks/
  Stores exploratory and analytical Jupyter notebooks.

### Data Quality Summary

- Target: 400+ reviews per bank
- Total target: 1,200+ reviews
- Missing values were removed during preprocessing
- Duplicate reviews were removed before export

### Limitations

- Google Play reviews may change over time as users edit or delete reviews
- Some apps may provide fewer reviews depending on availability and scraper limitations
- Only publicly available reviews from Google Play were analyzed

---

## Project Structure

```text
fintech-review-analytics/
├── .github/workflows/
├── data/raw/
├── notebooks/
├── scripts/
├── src/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore