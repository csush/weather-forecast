from rest_framework import serializers


class PlanHolidayInSerializer(serializers.Serializer):
    destinations = serializers.ListField(child=serializers.CharField())
    start_date = serializers.DateField()
    end_date = serializers.DateField()


class WeatherDailySerializer(serializers.Serializer):
    time = serializers.ListField(child=serializers.DateField())
    temperature_2m_max = serializers.ListField(child=serializers.FloatField())
    temperature_2m_min = serializers.ListField(child=serializers.FloatField())


class PlanHolidayOutSingleSerializer(serializers.Serializer):
    name = serializers.CharField()
    country = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    forecasts = WeatherDailySerializer()
    historical_weather = WeatherDailySerializer()


class PlanHolidayOutManySerializer(serializers.Serializer):
    results = PlanHolidayOutSingleSerializer(many=True)