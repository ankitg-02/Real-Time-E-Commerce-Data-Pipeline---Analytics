
api_dict={
    "dummyjson":"https://dummyjson.com/products",
    "fakestoreapi":"https://fakestoreapi.com/products"
}

class DataSource:
    def __init__(self, source_name):
        self.source_name = source_name
        self.api_url = api_dict.get(source_name, None)
        if self.api_url is None:
            raise ValueError(f"Data source '{source_name}' not found in API dictionary.")

#dynamic data source list
for source in api_dict.keys():
    try:
        data_source = DataSource(source)
        print(f"Data source '{source}' initialized with API URL: {data_source.api_url}")
    except ValueError as e:
        print(e)