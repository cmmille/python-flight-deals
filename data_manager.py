import dotenv
import os
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    dotenv.load_dotenv()

    def __init__(self):
        api_key = os.getenv('SHEETY_API')
        bearer_token = os.getenv('SHEETY_TOKEN')
        self.url = f"https://api.sheety.co/{api_key}/flightDeals/flights"
        self.headers = {"Authorization": bearer_token}

    def read_sheet(self):
        res = requests.get(url=self.url, headers=self.headers)
        res.raise_for_status()
        return res.json()

    def update_airport(self, flight):
        id = flight['id']
        put_url = f"{self.url}/{id}"
        body = {'flight': flight}
        res = requests.put(url=put_url, headers=self.headers, json=body)
        res.raise_for_status()

