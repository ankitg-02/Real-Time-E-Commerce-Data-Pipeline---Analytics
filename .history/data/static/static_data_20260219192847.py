import pandas as pd

file_path=["data\static\FashionDataset.csv",
           "data\static\flipkart_com-ecommerce_sample.csv",
           "data\static\myntra_dataset_ByScraping.csv"]
class StaticData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()
    def load_data(self):
        try:
            data = pd.read_csv(self.file_path)
            print(f"Static data loaded successfully from {self.file_path}")
            return data
        except Exception as e:
            print(f"Error loading static data: {e}")
            return None
        
        # Load static data from CSV selffil
        
