import os
import asyncio
from typing import List
import httpx
from weather_forecast.models import GeocodeModel, WeatherModel


class GeocodingService:
    def __init__(self):
        self.geocoding_api_url = os.getenv("GEOCODING_API_URL")

    def _create_request_params(self, city: str) -> dict:
        return {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

    async def _get_geocoding(self, client: httpx.AsyncClient, city: str) -> dict:
        url = self.geocoding_api_url.format(city)
        query_params = self._create_request_params(city)

        try:
            response = await client.get(url, params=query_params)

            name = response.json()["results"][0]["name"]
            country = response.json()["results"][0]["country"]
            latitude = response.json()["results"][0]["latitude"]
            longitude = response.json()["results"][0]["longitude"]

            geocoding = {
                "name": name,
                "country": country,
                "latitude": latitude,
                "longitude": longitude
            }
            return geocoding

        except Exception as e:
            raise Exception(f"Error fetching geocoding for {city}: {e}")
    
    '''
    The `asyncio.gather()` function ensures that the sequence of output of results matches
    the sequence of the input of tasks. This is important for the
    `ForecastModel.from_response_to_objects()` method to work correctly.
    '''
    async def _get_geocoding_async(self, cities: List[str]):
        async with httpx.AsyncClient() as client:
            tasks = [self._get_geocoding(client, city) for city in cities]
            results = await asyncio.gather(*tasks)
            return results
        
    def run(self, cities) -> List[GeocodeModel]:
        geocode_data = asyncio.run(self._get_geocoding_async(cities))
        return GeocodeModel.from_list_to_objects(geocode_data=geocode_data)


class ForecastingService:
    def __init__(self):
        self.open_meteo_api_url = os.getenv("OPEN_METEO_API_URL")

    def _create_request_params(
        self,
        geocode_objs: List[GeocodeModel],
        forecast_days: int
    ) -> dict:
        return {
            "latitude": ','.join(str(obj.latitude) for obj in geocode_objs),
            "longitude": ','.join(str(obj.longitude) for obj in geocode_objs),
            "daily": "temperature_2m_max,temperature_2m_min",
            "forecast_days": forecast_days
        }
    
    def get_forecast(
        self,
        geocode_objs: List[GeocodeModel],
        forecast_days: int = 7
    ) -> List[WeatherModel]:
        url = self.open_meteo_api_url
        query_params = self._create_request_params(geocode_objs, forecast_days)
        response = httpx.get(url, params=query_params)

        return WeatherModel.from_response_to_objects(
            geocode_objs=geocode_objs,
            response=response.json()
        )


class HistoricalWeatherService:
    def __init__(self):
        self.historical_data_api_url = os.getenv("HISTORICAL_DATA_API_URL")

    def _create_request_params(
        self,
        geocode_objs: List[GeocodeModel],
        start_date: str,
        end_date: str
    ) -> dict:
        return {
            "latitude": ','.join(str(obj.latitude) for obj in geocode_objs),
            "longitude": ','.join(str(obj.longitude) for obj in geocode_objs),
            "start_date": start_date,
            "end_date": end_date,
            "daily": "temperature_2m_max,temperature_2m_min"
        }
    
    def get_historical_weather(
        self,
        geocode_objs: List[GeocodeModel],
        start_date,
        end_date
    ) -> List[WeatherModel]:
        url = self.historical_data_api_url
        query_params = self._create_request_params(geocode_objs, start_date, end_date)
        response = httpx.get(url, params=query_params)
        return WeatherModel.from_response_to_objects(
            geocode_objs=geocode_objs,
            response=response.json()
        )
