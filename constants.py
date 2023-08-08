import os
import datetime


# Datalake
data_lake_folder = "datalake"
parquet_files_folder = os.path.join(data_lake_folder, "parquet_files")
csv_files_folder = os.path.join(data_lake_folder, "csv_files")
duckdb_files_folder = os.path.join(data_lake_folder, "duckdb_files")

# Misc Data
synthetic_data_folder = "data"
customers_data_file = os.path.join(synthetic_data_folder, "customers.csv")
indian_food_data_file = os.path.join(synthetic_data_folder, "indian_food.csv")
products_data_file = os.path.join(synthetic_data_folder, "products.csv")
synthetic_data_output_file = os.path.join(synthetic_data_folder, "transactions.csv")
salesperson_data_file = os.path.join(synthetic_data_folder, "salesperson.csv")
random_date_start = datetime.datetime(2022, 1, 1).timestamp()
random_date_end = datetime.datetime.now().timestamp()

# Misc Data DDL(Create) Queries
database_path = os.path.join(duckdb_files_folder, "sales_data.db")
schema_name = "sales"
customers_table_name = "customers"
products_table_name = "products"
salesperson_table_name = "salesperson"
transactions_table_name = "transactions"

schema_query = """CREATE SCHEMA IF NOT EXISTS sales;"""
customers_table_query = """CREATE TABLE IF NOT EXISTS {0}.{1}(customer_id INTEGER,
                                                                customer_name VARCHAR,
                                                                email VARCHAR,
                                                                PRIMARY KEY(customer_id));""".format(schema_name, customers_table_name)

products_table_query = """CREATE TABLE IF NOT EXISTS {0}.{1}(product_id INTEGER,
                                                              product_name VARCHAR,
                                                              PRIMARY KEY(product_id));""".format(schema_name, products_table_name)

salesperson_table_query = """CREATE TABLE IF NOT EXISTS {0}.{1}(salesperson_id INTEGER,
                                                                    salesperson_name VARCHAR,
                                                                    PRIMARY KEY(salesperson_id));""".format(schema_name, salesperson_table_name)

transactions_table_query = """CREATE TABLE IF NOT EXISTS {0}.{1}(invoice_line_item_id VARCHAR,
                                                                      product_id INTEGER,
                                                                      customer_id INTEGER,
                                                                      salesperson_id INTEGER,
                                                                      invoice_date INTEGER,
                                                                      quantity INTEGER,
                                                                      net_amount INTEGER,
                                                                      invoice_id VARCHAR,
                                                                      PRIMARY KEY(invoice_line_item_id));""".format(schema_name, transactions_table_name)
