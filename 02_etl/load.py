import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://localhost:5432/ecommerce_dw")

print("Loading data...")

dim_users = pd.read_csv("01_data/processed/dim_users.csv")
dim_date = pd.read_csv("01_data/processed/dim_date.csv")
fact_orders = pd.read_csv("01_data/processed/fact_orders.csv")

with engine.begin() as conn:
    conn.execute(text("DROP TABLE IF EXISTS fact_orders CASCADE"))
    conn.execute(text("DROP TABLE IF EXISTS dim_users CASCADE"))
    conn.execute(text("DROP TABLE IF EXISTS dim_date CASCADE"))

# Load dimension tables first
dim_users.to_sql("dim_users", engine, if_exists="replace", index=False)
print("dim_users loaded")

dim_date.to_sql("dim_date", engine, if_exists="replace", index=False)
print("dim_date loaded")

# Load fact table last
fact_orders.to_sql("fact_orders", engine, if_exists="replace", index=False)
print("fact_orders loaded")

print("Star schema tables loaded into PostgreSQL successfully.")