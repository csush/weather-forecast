import pytest
from weather_forecast.services import GeocodingService, ForecastingService, HistoricalWeatherService


@pytest.fixture
def geocoding_service():
    return GeocodingService()

@pytest.fixture
def forecasting_service():
    return ForecastingService()

@pytest.fixture
def historical_weather_service():
    return HistoricalWeatherService()