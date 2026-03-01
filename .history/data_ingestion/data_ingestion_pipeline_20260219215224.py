from data.static.static_data import StaticData
from data.dynamic.data_source import DataSource

class DataIngestionPipeline:
    def __init__(self):
        self.static_data = []
        self.dynamic_data_sources = []
    def load_static_data(self, file_paths):