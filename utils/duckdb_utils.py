import duckdb
import traceback

class Duckdb_utils:
    def __init__(self):
        self.con_obj = None

    def connect_to_db(self, db_path, read_only=False, in_memory=False):
        try:
            if in_memory:
                # to start an in-memory database
                self.con_obj = duckdb.connect(database=":memory:")
            else:
                # if read_only = True, then the database file can be shared between processes else not; related to semaphore lock by duckdb
                self.con_obj = duckdb.connect(db_path, read_only=read_only)
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))

    def close_connections(self):
        try:
            self.con_obj.close()
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))

    def execute_query(self, query):
        result = None
        try:
            result = self.con_obj.sql(query)
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
        return result
