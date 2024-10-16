# Weather Forecast

A company is building a holiday planner. Customers can choose a sequence of destinations as a schedule, taking the weather at each location into account.

An API that takes as input a list of destinations and dates, and returns a list of weather forecasts for each destination on each date.

## API

### GET /forecast

#### Parameters

- `destinations`: A list of destinations to get weather forecasts for.
- `dates`: A list of dates to get weather forecasts for.

#### Response

```json
{
  "destinations": [
    {
      "name": "New York",
      "forecasts": [
        {
          "date": "2023-01-01",
          "temperature": 20,
          "humidity": 50,
          "wind_speed": 10
        },
        {
          "date": "2023-01-02",
          "temperature": 22,
          "humidity": 60,
          "wind_speed": 12
        }
      ]
    },
    {
      "name": "London",
      "forecasts": [
        {
          "date": "2023-01-01",
          "temperature": 15,
          "humidity": 70,
          "wind_speed": 5
        },
        {
          "date": "2023-01-02",
          "temperature": 18,
          "humidity": 80,
          "wind_speed": 7
        }
      ]
    }
  ]
}
```

## Running the tests

To run the tests, run the following command:

```bash
python -m pytest
```

## Running the application

To run the application, run the following command:

```bash
uvicorn weather_forecast.asgi:application --reload
```