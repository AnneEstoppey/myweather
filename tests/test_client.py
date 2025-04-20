# Checking that if the API is down or returns a 401 Unauthorized, 
# WeatherClient.get_weather() doesn't silently fail — it should raise a proper exception.
import pytest
from myweather.client import WeatherClient
import requests


class FakeErrorResponse:
    def raise_for_status(self):
        raise requests.exceptions.HTTPError("401 Client Error: Unauthorized")


def fake_get_error(*args, **kwargs):
    return FakeErrorResponse()


def test_get_weather_http_error(monkeypatch):
    monkeypatch.setattr(requests, "get", fake_get_error)

    client = WeatherClient(token="invalid-token")

    with pytest.raises(requests.exceptions.HTTPError) as exc_info:
        client.get_weather("Oslo")

    assert "401" in str(exc_info.value)