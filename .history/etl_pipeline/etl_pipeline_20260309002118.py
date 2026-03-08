from data_ingestion.data_ingestion_pipeline import DataIngestionPipeline
class ETLPipeline:
    def __init__(self):
        self.data_ingestion_pipeline = DataIngestionPipeline()
    def extact(self):
        # Load static data
        file_paths = ["data/static/FashionDataset.csv", "data/static/flipkart_com-ecommerce_sample.csv", "data/static/myntra_dataset_ByScraping.csv"]
        self.data_ingestion_pipeline.load_static_data(file_paths)
        # Initialize dynamic data sources
        source_names = ["dummyjson", "fakestoreapi"]
        self.data_ingestion_pipeline.initialize_dynamic_data_sources(source_names)
    def transform(self):
        # Placeholder for transformation logic
        pass
    def load(self):
        # Placeholder for loading logic
        pass
if __name__ == "__main__":    etl_pipeline = ETLPipeline()