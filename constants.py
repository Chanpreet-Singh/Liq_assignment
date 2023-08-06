import os
import datetime

# Misc Data
synthetic_data_folder = "data"
customers_data_file = os.path.join(synthetic_data_folder, "customers.csv")
indian_food_data_file = os.path.join(synthetic_data_folder, "indian_food.csv")
products_data_file = os.path.join(synthetic_data_folder, "products.csv")
synthetic_data_output_file = os.path.join(synthetic_data_folder, "transactions.csv")
random_date_start = datetime.datetime(2022, 1, 1).timestamp()
random_date_end = datetime.datetime.now().timestamp()

# Datalake
data_lake_folder = "datalake"
parquet_files_folder = os.path.join(data_lake_folder, "parquet_files")
csv_files_folder = os.path.join(data_lake_folder, "csv_files")