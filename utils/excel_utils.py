import traceback

import pandas as pd

from utils import file_utils

class csv_io:
    def read_csv_file(self, file_path):
        df = pd.DataFrame()
        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
        return df

    def dump_csv_file(self, data, file_path, need_header=True, need_index=False):
        status = False
        try:
            data.to_csv(file_path, header=need_header, index=need_index)
            if file_utils.get_file_size(file_path) > 0:
                status = True
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
        return status

class excel_io:
    def read_excel_file(self, file_path):
        df = pd.DataFrame()
        try:
            df = pd.read_excel(file_path)
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
        return df

    def dump_excel_file(self, data, file_path, need_header=True, need_index=False):
        status = False
        try:
            data.to_excel(file_path, header=need_header, index=need_index)
            if file_utils.get_file_size(file_path) > 0:
                status = True
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
        return status