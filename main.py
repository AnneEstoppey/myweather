import os
from dotenv import load_dotenv
from myweather import WeatherClient
import logging
import argparse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Fetch current weather for a given city.")
    parser.add_argument(
        "--city", 
        type=str, 
        default="Tananger",
        help="City name to fetch weather for (default: Tananger)"
    )
    args = parser.parse_args()
    city = args.city

    # Load API token from environment variables
    load_dotenv()
    token = os.getenv("WEATHERSTACK_TOKEN")

    if not token:
        raise ValueError("Missing WEATHERSTACK_TOKEN in environment")

    # Call API
    client = WeatherClient(token)
    weather = client.get_weather(city)

    if weather is None:
        logging.warning("No weather data returned.")
    else:
        print(f"\nWeather for {weather.location.name}, {weather.location.country}:\n")
        print(f"Temperature: {weather.current.temperature}°C")
        print(f"Conditions: {', '.join(weather.current.weather_descriptions)}")
        print(f"Wind Speed: {weather.current.wind_speed} km/h")
        print(f"Wind Direction: {weather.current.wind_dir}")
        print(f"Pressure: {weather.current.pressure} hPa")
        print(f"Precipitation: {weather.current.precip} mm\n")
        print("Weather data retrieved successfully.")
if __name__ == "__main__":
    main()
