## 🧪 Weather Client Project — Summary

This project is a simple Python weather client that fetches current weather data from the [WeatherStack API](https://weatherstack.com/) and models the response using **Pydantic**.

### 🗂️ Project Structure

<pre>
myweather/
├── main.py                  # App entry point
├── .env                     # Contains WEATHERSTACK_TOKEN (not committed)
├── pyproject.toml           # Dependency and package config
├── uv.lock                  # Locked dependencies
├── myweather/
│   ├── __init__.py
│   ├── client.py            # WeatherClient class with logging + error handling
│   └── models.py            # Pydantic models for typed weather response
└── tests/
    └── test_client.py       # Unit tests with pytest
</pre>



### 🔐 Secret Management

- The API token is stored in `.env` and loaded using `python-dotenv`
- `.env` is added to `.gitignore`
- Loaded in `main.py` using `os.getenv("WEATHERSTACK_TOKEN")`

### 🔧 WeatherClient Class

Defined in `myweather/client.py`:

- Calls `http://api.weatherstack.com/current`
- Handles:
  - `HTTPError`
  - `ConnectionError`
  - `Timeout`
  - `RequestException`
  - `Pydantic ValidationError`
- Returns a `WeatherResponse` Pydantic model on success, or `None` on failure
- Uses `logging` instead of `print()` for all diagnostics

### 🧱 Pydantic Models

Defined in `myweather/models.py`:

```python
from pydantic import BaseModel
from typing import List

class CurrentWeather(BaseModel):
    temperature: int
    weather_descriptions: List[str]

class Location(BaseModel):
    name: str
    country: str

class WeatherResponse(BaseModel):
    location: Location
    current: CurrentWeather
```

### 🧪 Unit Testing with `pytest`

Unit tests are located in the `tests/` folder and use `pytest` for simple testing of the `WeatherClient`.

- `monkeypatch` is used to **mock** the `requests.get` call
- The test checks both:
  - Successful weather response
  - Handling of HTTP errors

#### ✅ Example test (`tests/test_client.py`)

```python
def fake_get_error(*args, **kwargs):
    class FakeResponse:
        def raise_for_status(self):
            raise requests.exceptions.HTTPError("401 Client Error: Unauthorized")
    return FakeResponse()

def test_get_weather_http_error_handled(monkeypatch):
    import requests
    monkeypatch.setattr(requests, "get", fake_get_error)

    client = WeatherClient(token="invalid")
    result = client.get_weather("Oslo")

    assert result is None
```

### ✅ Future Ideas

- [ ] **Expand Pydantic models**  
  Add support for more fields from the API, such as:
  - Wind speed
  - Humidity
  - "Feels like" temperature
  - Moon phase, visibility, etc.

- [ ] **Add a CLI interface**  
  Use `argparse` to allow passing the city as a command-line argument:
  ```bash
  python main.py --city Oslo


