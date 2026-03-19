from google.cloud import bigquery
import os
import pandas as pd

# Google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

# BigQuery client
client = bigquery.Client()

# Query ecommerce-style public dataset
query = """
SELECT
  order_id,
  user_id,
  status,
  gender,
  created_at,
  returned_at,
  shipped_at,
  delivered_at,
  num_of_item
FROM `bigquery-public-data.thelook_ecommerce.orders`
LIMIT 5000
"""

# Run query and store in dataframe
df = client.query(query).to_dataframe()

# Create raw data folder if needed
os.makedirs("01_data/raw", exist_ok=True)

# Save raw extract
output_path = "01_data/raw/orders_raw.csv"
df.to_csv(output_path, index=False)

print("Data extracted successfully.")
print(f"Saved to: {output_path}")
print(df.head())
print(df.shape)