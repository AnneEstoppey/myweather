# Core logic

import requests

class WeatherClient:
    def __init__(self, token: str):
        self.base_url = "http://api.weatherstack.com/current"
        self.token = token

    def get_weather(self, city: str) -> dict:
        params = {
            "access_key": self.token,
            "query": city
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()
