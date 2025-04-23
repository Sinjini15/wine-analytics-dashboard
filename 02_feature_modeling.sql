-- Average rating by country
SELECT
    country,
    COUNT(*) AS review_count,
    AVG(points) AS avg_score
FROM wine_reviews
GROUP BY country
ORDER BY avg_score DESC
LIMIT 10;
