import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://localhost:5432/ecommerce_dw")

print("Reading processed files...")

dim_users = pd.read_csv("01_data/processed/dim_users.csv")
dim_date = pd.read_csv("01_data/processed/dim_date.csv")
fact_orders = pd.read_csv("01_data/processed/fact_orders.csv")

print("Creating schema...")

with engine.begin() as conn:
    schema_sql = open("03_sql/schema.sql", "r").read()
    conn.execute(text(schema_sql))

print("Loading dimension tables...")
dim_users.to_sql("dim_users", engine, if_exists="append", index=False)
dim_date.to_sql("dim_date", engine, if_exists="append", index=False)

print("Loading fact table...")
fact_orders.to_sql("fact_orders", engine, if_exists="append", index=False)

print("Warehouse tables loaded successfully with schema, constraints, and indexes.")