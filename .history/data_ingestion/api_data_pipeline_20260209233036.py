import requests
import json

api_url = "https://fakestoreapi.com/products"  # Replace with your actual API URL
data = requests.get(api_url).json()
