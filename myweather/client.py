# Core logic

import requests
import logging
from typing import Optional
from .models import WeatherResponse
from pydantic import ValidationError

logger = logging.getLogger(__name__)


class WeatherClient:
    """
    A client for the WeatherStack API.
    """
    def __init__(self, token: str):
        self.base_url = "http://api.weatherstack.com/current"
        self.token = token


    def get_weather(self, city: str) -> Optional[WeatherResponse]:
        params = {
            "access_key": self.token,
            "query": city
        }
        try:
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            return WeatherResponse(**data)

        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error occurred: {e}")
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error occurred: {e}")
        except requests.exceptions.Timeout as e:
            logger.error(f"Request timed out: {e}")
        except requests.exceptions.RequestException as e:
            logger.error(f"An unexpected error occurred: {e}")
        except Exception as e:
            logger.error(f"Failed to parse weather data: {e}")
        except ValidationError as e:
            logger.error(f"Invalid API response format: {e}")

        return None
        # If the API fails, return None