import os
from dotenv import load_dotenv
from myweather import WeatherClient
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    load_dotenv()  # Loads from .env
    token = os.getenv("WEATHERSTACK_TOKEN")

    if not token:
        raise ValueError("Missing WEATHERSTACK_TOKEN in environment")

    client = WeatherClient(token)
    city = "Tananger"
    weather = client.get_weather(city)
    if weather is None:
        logging.warning("No weather data returned.")
    else:
        print(f"\nWeather for {weather.location.name}, {weather.location.country}:\n")
        print(f"Temperature: {weather.current.temperature}°C")
        print(f"Conditions: {', '.join(weather.current.weather_descriptions)}")

if __name__ == "__main__":
    main()
    