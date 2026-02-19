import pandas as pd

class StaticData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()
    def load_data(self):
        
        # Load static data from CSV selffil
