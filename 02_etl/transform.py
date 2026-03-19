import pandas as pd
import os


def transform_orders(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    print("Raw shape:", df.shape)
    print("\nMissing values:")
    print(df.isna().sum())

    # Convert datetime columns
    datetime_cols = ["created_at", "returned_at", "shipped_at", "delivered_at"]
    for col in datetime_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # Standardize text columns
    df["status"] = df["status"].astype(str).str.strip().str.lower()
    df["gender"] = df["gender"].astype(str).str.strip().str.lower()

    # Basic cleaning rules
    df = df.drop_duplicates()
    df = df[df["num_of_item"] > 0]

    # Derived columns
    df["order_date"] = df["created_at"].dt.date
    df["order_year"] = df["created_at"].dt.year
    df["order_month"] = df["created_at"].dt.month
    df["order_day"] = df["created_at"].dt.day

    # Save cleaned data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print("\nCleaned shape:", df.shape)
    print(f"Saved cleaned data to: {output_path}")

    return df


if __name__ == "__main__":
    transform_orders(
        input_path="01_data/raw/orders_raw.csv",
        output_path="01_data/processed/orders_cleaned.csv"
    )