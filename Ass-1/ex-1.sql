CREATE TABLE sale (
    product_id INT,
    date DATE,
    revenue NUMERIC(10, 2)
);
INSERT INTO sale (product_id, date, revenue) VALUES
(1, '2024-01-01', 100.50),
(2, '2024-01-02', 200.75),
(1, '2024-02-01', 300.25),
(3, '2024-01-03', 150.00),
(2, '2024-02-15', 250.00),
(1, '2024-03-01', 400.00),
(4, '2024-03-10', 500.00),
(5, '2024-04-01', 300.00),
(3, '2024-02-10', 350.50),
(5, '2024-05-01', 450.00);
SELECT product_id, SUM(revenue) AS total_revenue, MAX(date) AS latest_sale_date
FROM sale
GROUP BY product_id
ORDER BY total_revenue DESC, latest_sale_date DESC
LIMIT 5;