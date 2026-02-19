import pandas as pd

class StaticData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()
        
        # Load static data from CSV selffil
