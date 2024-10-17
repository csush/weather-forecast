from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta

from .serializers import (
    PlanHolidayInSerializer,
    PlanHolidayOutManySerializer
)

from weather_forecast.services import (
    GeocodingService,
    ForecastingService,
    HistoricalWeatherService
)


class PlanHolidayView(APIView):
    """
    Plan your holiday
    """
    def get(self, request, format=None):
        serializer = PlanHolidayInSerializer(data=request.data)
        if serializer.is_valid():
            destinations = serializer.data["destinations"]
            start_date = serializer.data["start_date"]
            end_date = serializer.data["end_date"]
            geocoding_service = GeocodingService()
            forecasting_service = ForecastingService()
            historical_weather_service = HistoricalWeatherService()

            try:
                geocoded_cities = geocoding_service.run(destinations)
                forecasted_weather = forecasting_service.get_forecast(geocoded_cities)
                start_date_minus_one_year = datetime.strptime(start_date, "%Y-%m-%d") - timedelta(days=365)
                end_date_minus_one_year = datetime.strptime(end_date, "%Y-%m-%d") - timedelta(days=365)
                historical_weather = historical_weather_service.get_historical_weather(
                    geocoded_cities,
                    start_date_minus_one_year.strftime(format="%Y-%m-%d"),
                    end_date_minus_one_year.strftime(format="%Y-%m-%d")
                )

                out_list = []
                for i in range(len(geocoded_cities)):
                    data = {
                            "name": geocoded_cities[i].name,
                            "country": geocoded_cities[i].country,
                            "latitude": geocoded_cities[i].latitude,
                            "longitude": geocoded_cities[i].longitude,
                            "forecasts": forecasted_weather[i].daily.to_dict(),
                            "historical_weather": historical_weather[i].daily.to_dict()
                    }
                    out_list.append(data)

                out_serializer = PlanHolidayOutManySerializer(data={"results": out_list})
                if out_serializer.is_valid():
                    return Response(out_serializer.data)
                else:
                    return Response(out_serializer.errors, status=400)
            except Exception as e:
                return Response({"error": str(e)}, status=400)