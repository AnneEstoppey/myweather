from pydantic import BaseModel
from typing import List


class Location(BaseModel):
    name: str
    country: str


class CurrentWeather(BaseModel):
    temperature: int
    weather_descriptions: List[str]


class WeatherResponse(BaseModel):
    location: Location
    current: CurrentWeather
