import pandas as pd

import constants
from utils import excel_utils
from utils import random_utils

"""
This script will generate syntetic data in a csv format containing the following fields:

invoice_line_item_id = tx_id
product_id
customer_id
invoice_date = tx_date (ie: YYYYMMDD)
quantity
net_amount
invoice_id (allows us to group the invoice_line_items)
"""

class Randomdatagenerator():
    def __init__(self):
        self.total_products = self.get_product_list()

    def get_product_list(self):
        recipe_data = excel_utils.read_csv_file(constants.indian_food_data_file)
        product_data = []
        for ind, each_data in recipe_data.iterrows():
            ff = {"product_id": ind + 1,
                  "product_name": each_data["name"]
                  }
            product_data.append(ff)
        product_df = pd.DataFrame(product_data)
        excel_utils.dump_csv_file(product_df, constants.products_data_file)
        return len(product_data)

    def get_invoice_items(self, invoice_id, items_per_transaction):
        invoice = []
        for i in range(items_per_transaction):
            data = {
                        "invoice_line_item_id": "{0}_{1}".format(invoice_id, i+1),
                        "product_id": random_utils.get_random_number(1, self.total_products),
                        "customer_id": random_utils.get_random_number(1, 20),
                        "salesperson_id": random_utils.get_random_number(1, 8),
                        "invoice_date": int(random_utils.get_random_date(constants.random_date_start, constants.random_date_end).strftime("%Y%m%d")),
                        "quantity": random_utils.get_random_number(1, 10),
                        "net_amount": random_utils.get_random_number(15, 50),
                        "invoice_id": invoice_id
                   }
            invoice.append(data)
        return invoice

    def generate_random_data(self, num_records):
        list_of_data = []
        count = 1
        while count <= num_records:
            items_per_transaction = random_utils.get_random_number(1, 5)
            invoice_id = random_utils.get_unique_random_string(10)
            invoice_list = self.get_invoice_items(invoice_id, items_per_transaction)
            list_of_data.extend(invoice_list)
            count += items_per_transaction
            print(count)
        df = pd.DataFrame(list_of_data)
        del(list_of_data)
        excel_utils.dump_csv_file(df, constants.synthetic_data_output_file)

if __name__ == '__main__':
    num_records = 3*365*10000  # Number of records to generate
    cls_obj = Randomdatagenerator()
    generated_data = cls_obj.generate_random_data(num_records)
