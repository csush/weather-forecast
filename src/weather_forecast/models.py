from typing import List


class GeocodeModel:
    def __init__(self, geocode_data: dict):
        self.name = geocode_data["name"]
        self.country = geocode_data["country"]
        self.latitude = geocode_data["latitude"]
        self.longitude = geocode_data["longitude"]

    def __repr__(self) -> str:
        return f"GeocodeModel(name={self.name})"
    
    @staticmethod
    def from_list_to_objects(geocode_data: List[dict]):
        return [GeocodeModel(geocode_data=geocode) for geocode in geocode_data]


class WeatherDailyModel:
    def __init__(self, daily_data: dict) -> None:
        self.time = daily_data["time"]
        self.temperature_2m_max = daily_data["temperature_2m_max"]
        self.temperature_2m_min = daily_data["temperature_2m_min"]

    def __repr__(self) -> str:
        return f"WeatherDailyModel(time={self.time}, temperature_2m_max={self.temperature_2m_max}, temperature_2m_min={self.temperature_2m_min})"


class WeatherModel:
    def __init__(self, weather_data: dict) -> None:
        self.geocode_model = weather_data["geocode_model"]
        self.daily = weather_data["daily"]
    
    def __repr__(self) -> str:
        return f"WeatherModel(geocode_model={self.geocode_model}, daily={self.daily})"

    @staticmethod
    def from_response_to_objects(geocode_objs: List[GeocodeModel], response: List[dict]):
        if len(geocode_objs) != len(response):
            raise Exception("Length of geocode objects and response objects should be equal")
        
        combined_weather_data = [
            {
                "geocode_model": geocode_objs[i],
                "daily": WeatherDailyModel(daily_data=response[i]["daily"])
            } for i in range(len(geocode_objs))
        ]
        return [WeatherModel(weather_data=weather_data) for weather_data in combined_weather_data]
