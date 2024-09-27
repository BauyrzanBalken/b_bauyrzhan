CREATE TABLE monthly_sales (
    year INT,
    month INT,
    total_sales NUMERIC(10, 2),
    region VARCHAR(50)
);
INSERT INTO monthly_sales (year, month, total_sales, region) VALUES
(2024, 1, 10000.00, 'North'),
(2024, 1, 15000.00, 'South'),
(2024, 2, 12000.00, 'North'),
(2024, 2, 13000.00, 'South'),
(2024, 3, 11000.00, 'North'),
(2024, 3, 16000.00, 'South'),
(2024, 1, 8000.00, 'East'),
(2024, 1, 9000.00, 'West'),
(2024, 2, 10000.00, 'East'),
(2024, 2, 11000.00, 'West');
SELECT year, month, region, SUM(total_sales) AS total_sales_for_region
FROM monthly_sales
GROUP BY year, month, region
ORDER BY year ASC, month ASC;