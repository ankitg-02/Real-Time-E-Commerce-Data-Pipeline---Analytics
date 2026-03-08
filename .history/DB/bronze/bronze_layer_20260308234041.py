
import pandas as pd
import os
from data_lake import DataLake

class BronzeLayer:
    def __init__(self, data_lake):
        self.data_lake = data_lake
        self.bronze_data = []
    def process_static_data(self):
        for df in self.data_lake.static_data:
            # Basic cleaning: drop duplicates and handle missing values
            df_cleaned = df.drop_duplicates().fillna(method='ffill')
            self.bronze_data.append(df_cleaned)

