DROP TABLE IF EXISTS fact_orders;
DROP TABLE IF EXISTS dim_users;
DROP TABLE IF EXISTS dim_date;

CREATE TABLE dim_users (
    user_id INT PRIMARY KEY,
    gender VARCHAR(20)
);

CREATE TABLE dim_date (
    date_id INT PRIMARY KEY,
    order_date DATE,
    order_year INT,
    order_month INT,
    order_day INT
);

CREATE TABLE fact_orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    date_id INT,
    status VARCHAR(50),
    num_of_item INT,
    FOREIGN KEY (user_id) REFERENCES dim_users(user_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);