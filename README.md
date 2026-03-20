# E-Commerce Data Warehouse & ETL Pipeline

## 📌 Project Overview
This project demonstrates an end-to-end data engineering pipeline that extracts e-commerce data from Google BigQuery, transforms it using Python, and loads it into a PostgreSQL data warehouse designed using a star schema.

---

## 🏗️ Architecture

BigQuery → Python ETL → CSV (Raw & Processed) → PostgreSQL → SQL Analytics

---

## ⚙️ Tech Stack
- Python (Pandas)
- Google BigQuery
- PostgreSQL
- SQL
- Git & GitHub

---

## 🔄 ETL Pipeline

### 1. Extract
- Data pulled from Google BigQuery public dataset (`thelook_ecommerce`)

### 2. Transform
- Data cleaning and validation
- Handling missing values
- Feature engineering (year, month, day)
- Standardizing categorical values

### 3. Load
- Loaded into PostgreSQL warehouse tables

---

## 🧱 Data Warehouse Design (Star Schema)

### Fact Table
- `fact_orders`

### Dimension Tables
- `dim_users`
- `dim_date`

---

## 📊 SQL Analytics

Implemented queries for:
- Order trends over time
- Sales distribution by status and gender
- Top users by activity
- Monthly and daily performance metrics

---

## 📁 Project Structure