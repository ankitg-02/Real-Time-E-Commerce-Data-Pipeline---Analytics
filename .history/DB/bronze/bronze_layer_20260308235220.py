
import pandas as pd
import os
from data_lake import DataLake

class BronzeLayer:
    def __init__(self, data_lake):
        self.data_lake = data_lake
        self.bronze_data = []
    def data_transfer(self):
        # Transfer static data to bronze layer
        for dataset in self.data_lake.static_data:
            self.bronze_data.append(dataset)
        # Transfer dynamic data sources to bronze layer
        for source in self.data_lake.dynamic_data_sources:
            self.bronze_data.append(source)

