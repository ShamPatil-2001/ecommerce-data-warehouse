import pandas as pd
import os


def transform_orders(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    print("Raw shape:", df.shape)
    print("\nMissing values:")
    print(df.isna().sum())

    datetime_cols = ["created_at", "returned_at", "shipped_at", "delivered_at"]
    for col in datetime_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    df["status"] = df["status"].astype(str).str.strip().str.lower()
    df["gender"] = df["gender"].astype(str).str.strip().str.lower()

    df = df.drop_duplicates()
    df = df[df["num_of_item"] > 0]

    df["order_date"] = df["created_at"].dt.date
    df["order_year"] = df["created_at"].dt.year
    df["order_month"] = df["created_at"].dt.month
    df["order_day"] = df["created_at"].dt.day

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print("\nCleaned shape:", df.shape)
    print(f"Saved cleaned data to: {output_path}")

    return df


def build_star_schema(df: pd.DataFrame):
    dim_users = df[["user_id", "gender"]].drop_duplicates().reset_index(drop=True)

    dim_date = (
        df[["order_date", "order_year", "order_month", "order_day"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    dim_date["date_id"] = dim_date.index + 1

    fact_orders = df.merge(dim_date, on=["order_date", "order_year", "order_month", "order_day"], how="left")

    fact_orders = fact_orders[["order_id", "user_id", "date_id", "status", "num_of_item"]]

    return dim_users, dim_date, fact_orders


if __name__ == "__main__":
    df_cleaned = transform_orders(
        input_path="01_data/raw/orders_raw.csv",
        output_path="01_data/processed/orders_cleaned.csv"
    )

    dim_users, dim_date, fact_orders = build_star_schema(df_cleaned)

    dim_users.to_csv("01_data/processed/dim_users.csv", index=False)
    dim_date.to_csv("01_data/processed/dim_date.csv", index=False)
    fact_orders.to_csv("01_data/processed/fact_orders.csv", index=False)

    print("Star schema files created successfully.")