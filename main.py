import os

print("Running ETL pipeline...")

os.system("python 02_etl/extract.py")
os.system("python 02_etl/transform.py")
os.system("python 02_etl/load.py")

print("ETL pipeline completed successfully.")