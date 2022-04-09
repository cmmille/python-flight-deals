import dotenv
import os
from datetime import datetime, timedelta

import requests

dotenv.load_dotenv()


class FlightSearch:
    def __init__(self):
        api = os.getenv('KIWI_API')
        self.url = "https://tequila-api.kiwi.com"
        self.header = {'apikey': api}

    def get_airport_info(self, query):
        url = f"{self.url}/locations/query"
        params = {'term': query,
                  'locale': 'en-US',
                  'location_types': 'city',
                  'limit': 1,
                  'active_only': 'true'
                  }
        res = requests.get(url, headers=self.header, params=params)
        res.raise_for_status()
        print(res.json())
        return res.json()

    def get_flight_info(self, city):
        url = f"{self.url}/v2/search"
        params = {
            'fly_from': 'DEN',
            'fly_to': city,
            'date_from': datetime.now().strftime("%d/%m/%Y"),
            'date_to': (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y"),
            'max_stopovers': 0,
            'curr': 'USD',
            'limit': 1,
            'nights_in_dst_from': 1,
            'nights_in_dst_to': 3,
            'one_for_city': 1,
            'flight_type': 'round'
        }
        res = requests.get(url, headers=self.header, params=params)
        res.raise_for_status()
        return res.json()['data'][0]
