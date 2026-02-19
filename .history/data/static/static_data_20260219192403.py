import pandas as pd

class StaticData:
    @staticmethod
    def load_static_data():
        # Load static data from CSV files
        products_df = pd.read_csv('data/static/products.csv')
        customers_df = pd.read_csv('data/static/customers.csv')
        return products_df, customers_df
