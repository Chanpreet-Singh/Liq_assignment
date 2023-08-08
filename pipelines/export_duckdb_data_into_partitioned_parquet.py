import os
from dagster import op, job

import constants
from utils import folder_utils
from utils.duckdb_utils import Duckdb_utils


@op
def create_db_connection():
    conn_obj = Duckdb_utils()
    conn_obj.connect_to_db(constants.database_path, read_only=True)
    return conn_obj

@op
def use_schema(conn_obj):
    if conn_obj is not None:
        conn_obj.execute_query("""USE {0};""".format(constants.schema_name))

@op
def create_folder_as_per_schema():
    folder_utils.create_folder(os.path.join(constants.parquet_files_folder, constants.schema_name))

@op
def export_data(conn_obj):
    if conn_obj is not None:
        file_path = os.path.join(constants.parquet_files_folder, constants.schema_name, constants.transactions_table_name)
        query = """COPY {2}.{0} TO '{1}' (FORMAT PARQUET, PARTITION_BY (salesperson_id, customer_id), OVERWRITE_OR_IGNORE 1);""".format(constants.transactions_table_name, file_path, constants.schema_name)
        conn_obj.execute_query(query)

@op
def close_db_connection(conn_obj):
    if conn_obj is not None:
        conn_obj.close_connections()

@job
def export_into_partitioned_parquet():
    db_conn = create_db_connection()
    use_schema(db_conn)
    create_folder_as_per_schema()
    export_data(db_conn)
    # close_db_connection(db_conn)

result = export_into_partitioned_parquet.execute_in_process()