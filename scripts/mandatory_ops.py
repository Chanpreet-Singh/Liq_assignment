import constants
from utils import folder_utils
class Mandatory_ops:
    def main(self, overwrite_datalake = False):
        if overwrite_datalake:
            folder_utils.remove_folder_tree(constants.data_lake_folder)
        folder_utils.create_folder(constants.data_lake_folder)
        folder_utils.create_folder(constants.parquet_files_folder)
        folder_utils.create_folder(constants.csv_files_folder)
        folder_utils.create_folder(constants.duckdb_files_folder)
