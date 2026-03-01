from data.static.static_data import StaticData
from data.dynamic.data_source import DataSource

class DataIngestionPipeline:
    def __init__(self):
        self.static_data = []
        self.dynamic_data_sources = []
    def load_static_data(self, file_paths):
        for path in file_paths:
            static_data = StaticData(path)
            self.static_data.append(static_data.data)
    def initialize_dynamic_data_sources(self, source_names):
        for source in source_names:
            try:
                data_source = DataSource(source)
                self.dynamic_data_sources.append(data_source)
            except ValueError as e:
                print(e)        