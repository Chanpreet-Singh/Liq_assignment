from dagster import op, job

import constants
from utils.duckdb_utils import Duckdb_utils
from scripts.mandatory_ops import Mandatory_ops

@op
def create_folders():
    Mandatory_ops().main()

@op
def create_db_connection():
    conn_obj = Duckdb_utils()
    conn_obj.connect_to_db(constants.database_path)
    return conn_obj

@op
def create_schema(conn_obj):
    if conn_obj is not None:
        conn_obj.execute_query(constants.schema_query)

@op
def create_tables(conn_obj):
    if conn_obj is not None:
        conn_obj.execute_query(constants.customers_table_query)
        conn_obj.execute_query(constants.products_table_query)
        conn_obj.execute_query(constants.salesperson_table_query)
        conn_obj.execute_query(constants.transactions_table_query)

@op
def ingest_data(conn_obj):
    if conn_obj is not None:
        print("Ingesting into {0}".format(constants.customers_table_name))
        conn_obj.execute_query("""COPY {0}.{1} FROM '{2}' (AUTO_DETECT TRUE);""".format(constants.schema_name, constants.customers_table_name, constants.customers_data_file))
        print("Ingesting into {0}".format(constants.products_table_name))
        conn_obj.execute_query("""COPY {0}.{1} FROM '{2}' (AUTO_DETECT TRUE);""".format(constants.schema_name, constants.products_table_name, constants.products_data_file))
        print("Ingesting into {0}".format(constants.salesperson_table_name))
        conn_obj.execute_query("""COPY {0}.{1} FROM '{2}' (AUTO_DETECT TRUE);""".format(constants.schema_name, constants.salesperson_table_name, constants.salesperson_data_file))
        print("Ingesting into {0}".format(constants.transactions_table_name))
        conn_obj.execute_query("""COPY {0}.{1} FROM '{2}' (AUTO_DETECT TRUE);""".format(constants.schema_name, constants.transactions_table_name, constants.synthetic_data_output_file))

@op
def close_db_connection(conn_obj):
    if conn_obj is not None:
        conn_obj.close_connections()

@job()
def my_data_pipeline():
    create_folders()
    db_conn = create_db_connection()
    create_schema(db_conn)
    create_tables(db_conn)
    ingest_data(db_conn)
    # close_db_connection(db_conn)

result = my_data_pipeline.execute_in_process()
