-- Create banks table

CREATE TABLE IF NOT EXISTS banks (

    bank_id SERIAL PRIMARY KEY,

    bank_name VARCHAR(255) NOT NULL,

    app_name VARCHAR(255) NOT NULL
);

-- Create reviews table

CREATE TABLE IF NOT EXISTS reviews (

    review_id SERIAL PRIMARY KEY,

    bank_id INTEGER REFERENCES banks(bank_id),

    review_text TEXT NOT NULL,

    rating INTEGER,

    review_date DATE,

    sentiment_label VARCHAR(50),

    sentiment_score FLOAT,

    identified_theme VARCHAR(255),

    source VARCHAR(100)
);