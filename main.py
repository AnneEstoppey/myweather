import os
from dotenv import load_dotenv
from myweather import WeatherClient

def main():
    load_dotenv()  # Loads from .env
    token = os.getenv("WEATHERSTACK_TOKEN")

    if not token:
        raise ValueError("Missing WEATHERSTACK_TOKEN in environment")

    client = WeatherClient(token)
    city = "Tananger"
    weather = client.get_weather(city)
    print(weather)

if __name__ == "__main__":
    main()
    