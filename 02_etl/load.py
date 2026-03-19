import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("01_data/processed/orders_cleaned.csv")

# PostgreSQL connection
engine = create_engine("postgresql://localhost:5432/ecommerce_dw")

# Load into table
df.to_sql("orders", engine, if_exists="replace", index=False)

print("Data loaded into PostgreSQL successfully.")