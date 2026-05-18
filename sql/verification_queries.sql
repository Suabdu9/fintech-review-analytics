-- Count reviews per bank

SELECT
    b.bank_name,
    COUNT(r.review_id) AS total_reviews
FROM reviews r
JOIN banks b
ON r.bank_id = b.bank_id
GROUP BY b.bank_name;


-- Average rating per bank

SELECT
    b.bank_name,
    AVG(r.rating) AS average_rating
FROM reviews r
JOIN banks b
ON r.bank_id = b.bank_id
GROUP BY b.bank_name;


-- Check for null review text

SELECT COUNT(*)
FROM reviews
WHERE review_text IS NULL;


-- Check for null sentiment labels

SELECT COUNT(*)
FROM reviews
WHERE sentiment_label IS NULL;