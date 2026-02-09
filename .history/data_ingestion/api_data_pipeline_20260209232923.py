import requests
import json

api_url = "https://fakestoreapi.com/products"  # Replace with your actual API URL
def fetch_api_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json() 
        print(# Parse the JSON response
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data from the API: {e}")
        return None