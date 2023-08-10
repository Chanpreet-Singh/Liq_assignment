import traceback
import pandas as pd

import constants
from utils.duckdb_utils import Duckdb_utils

class Dashboard_helper:
    def __init__(self):
        self.salesperson_id = None
        self.conn_obj = None
        self.create_conn_and_use_schema()

    def create_conn_and_use_schema(self):
        self.conn_obj = Duckdb_utils()
        self.conn_obj.connect_to_db(constants.database_path, read_only=True)
        self.conn_obj.execute_query("""USE {0};""".format(constants.schema_name))

    def get_all_salesperson_data(self):
        list_of_json = []
        try:
            query = """SELECT salesperson_id, salesperson_name from salesperson;"""
            result = self.conn_obj.execute_query(query)
            list_of_json = [{"label": each[1], "value": each[0]} for each in result.fetchall()]
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
        return list_of_json

    def get_salesperson_data(self, salesperson_id):
        op_df = pd.DataFrame()
        try:
            query = """SELECT MONTH(invoice_date) AS month, SUM(net_amount) AS Total_Amount FROM t1 WHERE YEAR(invoice_date)=2023 AND salesperson_id={0} GROUP BY month ORDER BY month""".format(salesperson_id)
            result = self.conn_obj.execute_query(query)
            op_df = result.to_df()
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
        return op_df
