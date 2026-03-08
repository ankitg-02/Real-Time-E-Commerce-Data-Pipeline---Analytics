import pandas as pd
from database import Database
class BronzeLayer(Database):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.table_name = "bronze_layer"

    def insert_data(self, data: pd.DataFrame):
        # Insert data into the bronze layer table
        self.insert_dataframe(self.table_name, data)

    def fetch_data(self):
        # Fetch data from the bronze layer table
        return self.fetch_all(self.table_name)