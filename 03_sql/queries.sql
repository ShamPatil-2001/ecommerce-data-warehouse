-- 1. Total orders by status
SELECT
    status,
    COUNT(*) AS total_orders
FROM fact_orders
GROUP BY status
ORDER BY total_orders DESC;

-- 2. Total items sold by status
SELECT
    status,
    SUM(num_of_item) AS total_items
FROM fact_orders
GROUP BY status
ORDER BY total_items DESC;

-- 3. Total orders by gender
SELECT
    u.gender,
    COUNT(f.order_id) AS total_orders
FROM fact_orders f
JOIN dim_users u
    ON f.user_id = u.user_id
GROUP BY u.gender
ORDER BY total_orders DESC;

-- 4. Total items sold by gender
SELECT
    u.gender,
    SUM(f.num_of_item) AS total_items
FROM fact_orders f
JOIN dim_users u
    ON f.user_id = u.user_id
GROUP BY u.gender
ORDER BY total_items DESC;

-- 5. Monthly order volume
SELECT
    d.order_year,
    d.order_month,
    COUNT(f.order_id) AS total_orders
FROM fact_orders f
JOIN dim_date d
    ON f.date_id = d.date_id
GROUP BY d.order_year, d.order_month
ORDER BY d.order_year, d.order_month;

-- 6. Monthly items sold
SELECT
    d.order_year,
    d.order_month,
    SUM(f.num_of_item) AS total_items
FROM fact_orders f
JOIN dim_date d
    ON f.date_id = d.date_id
GROUP BY d.order_year, d.order_month
ORDER BY d.order_year, d.order_month;

-- 7. Average items per order by status
SELECT
    status,
    ROUND(AVG(num_of_item), 2) AS avg_items_per_order
FROM fact_orders
GROUP BY status
ORDER BY avg_items_per_order DESC;

-- 8. Top 10 most active users by number of orders
SELECT
    user_id,
    COUNT(order_id) AS total_orders
FROM fact_orders
GROUP BY user_id
ORDER BY total_orders DESC
LIMIT 10;

-- 9. Top 10 users by total items ordered
SELECT
    user_id,
    SUM(num_of_item) AS total_items
FROM fact_orders
GROUP BY user_id
ORDER BY total_items DESC
LIMIT 10;

-- 10. Daily order volume
SELECT
    d.order_date,
    COUNT(f.order_id) AS total_orders
FROM fact_orders f
JOIN dim_date d
    ON f.date_id = d.date_id
GROUP BY d.order_date
ORDER BY d.order_date;

-- 11. Top 10 busiest dates by total orders
SELECT
    d.order_date,
    COUNT(f.order_id) AS total_orders
FROM fact_orders f
JOIN dim_date d
    ON f.date_id = d.date_id
GROUP BY d.order_date
ORDER BY total_orders DESC
LIMIT 10;

-- 12. Order distribution by year
SELECT
    d.order_year,
    COUNT(f.order_id) AS total_orders
FROM fact_orders f
JOIN dim_date d
    ON f.date_id = d.date_id
GROUP BY d.order_year
ORDER BY d.order_year;