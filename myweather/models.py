from pydantic import BaseModel
from typing import List


class Location(BaseModel):
    name: str
    country: str


class CurrentWeather(BaseModel):
    temperature: int
    weather_descriptions: List[str]
    wind_speed: int
    wind_degree: int
    wind_dir: str
    pressure: int
    precip: float


class WeatherResponse(BaseModel):
    location: Location
    current: CurrentWeather
