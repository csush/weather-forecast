from unittest.mock import patch, MagicMock
from ..models import GeocodeModel, WeatherModel
from .conftest import geocoding_service, forecasting_service, historical_weather_service


def test_geocoding_service_run(geocoding_service):
    mock_async_result = [
        {
            "name": "New York",
            "country": "United States",
            "latitude": 40.7128,
            "longitude": -74.0060
        }
    ]

    with patch('asyncio.run', return_value=mock_async_result):
        result = geocoding_service.run(["New York"])

    assert isinstance(result[0], GeocodeModel)
    assert result[0].name == "New York"
    assert result[0].country == "United States"
    assert result[0].latitude == 40.7128
    assert result[0].longitude == -74.0060

def test_forecasting_service(forecasting_service):
    mock_response = MagicMock()
    mock_response.json.return_value = [{
        "daily": {
            "time": ["2023-05-01", "2023-05-02"],
            "temperature_2m_max": [25.5, 26.7],
            "temperature_2m_min": [18.3, 19.1]
        }
    }]

    geocode_objs = [GeocodeModel({"name": "New York", "country": "United States", "latitude": 40.7128, "longitude": -74.0060})]

    with patch('httpx.get', return_value=mock_response):
        result = forecasting_service.get_forecast(geocode_objs)

    assert isinstance(result[0], WeatherModel)
    assert result[0].geocode_model == geocode_objs[0]
    assert result[0].daily.time == ["2023-05-01", "2023-05-02"]
    assert result[0].daily.temperature_2m_max == [25.5, 26.7]
    assert result[0].daily.temperature_2m_min == [18.3, 19.1]

def test_historical_weather_service(historical_weather_service):
    mock_response = MagicMock()
    mock_response.json.return_value = [{
        "daily": {
            "time": ["2022-05-01", "2022-05-02"],
            "temperature_2m_max": [24.5, 25.7],
            "temperature_2m_min": [17.3, 18.1]
        }
    }]

    geocode_objs = [GeocodeModel({"name": "New York", "country": "United States", "latitude": 40.7128, "longitude": -74.0060})]

    with patch('httpx.get', return_value=mock_response):
        result = historical_weather_service.get_historical_weather(geocode_objs, "2022-05-01", "2022-05-02")

    assert isinstance(result[0], WeatherModel)
    assert result[0].geocode_model == geocode_objs[0]
    assert result[0].daily.time == ["2022-05-01", "2022-05-02"]
    assert result[0].daily.temperature_2m_max == [24.5, 25.7]
    assert result[0].daily.temperature_2m_min == [17.3, 18.1]
