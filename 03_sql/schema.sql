DROP TABLE IF EXISTS fact_orders CASCADE;
DROP TABLE IF EXISTS dim_users CASCADE;
DROP TABLE IF EXISTS dim_date CASCADE;

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

CREATE INDEX idx_fact_orders_user_id ON fact_orders(user_id);
CREATE INDEX idx_fact_orders_date_id ON fact_orders(date_id);
CREATE INDEX idx_fact_orders_status ON fact_orders(status);

CREATE INDEX idx_dim_date_year_month ON dim_date(order_year, order_month);
CREATE INDEX idx_dim_users_gender ON dim_users(gender);