from google.cloud import bigquery
import os
import pandas as pd

# Set credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

# Create client
client = bigquery.Client()

print("Extracting data from BigQuery...")

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

df = client.query(query).to_dataframe()

# Save raw data
os.makedirs("01_data/raw", exist_ok=True)
df.to_csv("01_data/raw/orders_raw.csv", index=False)

print("Extraction complete.")
print(df.head())