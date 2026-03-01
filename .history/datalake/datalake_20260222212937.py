from data_ingestion import DataIngestion

class DataLake:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.static_data = []
        self.dynamic_data_sources = []
    def load_data(self):
        # Load static data
        file_paths = ["data/static/FashionDataset.csv", "data/static/flipkart_com-ecommerce_sample.csv", "data/static/myntra_dataset_ByScraping.csv"]
        self.data_ingestion.load_static_data(file_paths)
        self.static_data = self.data_ingestion.static_data
        # Initialize dynamic data sources
        source_names = ["dummyjson", "fakestoreapi"]
        self.data_ingestion.initialize_dynamic_data_sources(source_names)
        self.dynamic_data_sources = self.data_ingestion.dynamic_data_sources
if __name__ == "__main__":    data_lake = DataLake()