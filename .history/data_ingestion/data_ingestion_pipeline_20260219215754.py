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
if __name__ == "__main__":
    pipeline = DataIngestionPipeline()
    # Load static data
    file_paths = ["data/static/FashionDataset.csv", "data/static/flipkart_com-ecommerce_sample.csv", "data/static/myntra_dataset_ByScraping.csv"]
    pipeline.load_static_data(file_paths)
    # Initialize dynamic data sources
    source_names = ["dummyjson", "fakestoreapi"]
    pipeline.initialize_dynamic_data_sources(source_names)