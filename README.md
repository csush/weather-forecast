# Holiday Planner

An API that takes as input a list of destinations and a start and an end date. It returns a list of weather forecasts for each destination for the next 7 days, and the historical weather from 1 year before the start date to the end date.

## API

### GET /api/v1/plan

#### Parameters

- `destinations`: A list of destinations to get weather forecasts for.
- `start_date`: A string representing the start date in the format `YYYY-MM-DD`.
- `end_date`: A string representing the end date in the format `YYYY-MM-DD`.

#### Response

```json
[
  {
    "name": "New York",
    "country": "United States",
    "latitude": 52.52,
    "longitude": 13.41998,
    "forecasts": {
      "daily": {
        "time": [
          "2023-01-01",
          "2023-01-02",
          "2023-01-03",
          "2023-01-04",
          "2023-01-05",
          "2023-01-06",
          "2023-01-07"
        ],
        "temperature_2m_max": [
          20.0,
          22.0,
          23.0,
          24.0,
          25.0,
          26.0,
          27.0
        ],
        "temperature_2m_min": [
          15.0,
          17.0,
          18.0,
          19.0,
          20.0,
          21.0,
          22.0
        ]
      }
    },
    "historical_weather": {
      "daily": {
        "time": [
          "2022-01-01",
          "2022-01-02",
          "2022-01-03",
          "2022-01-04",
          "2022-01-05",
          "2022-01-06",
          "2022-01-07",
        ],
        "temperature_2m_max": [
          20.0,
          22.0,
          23.0,
          24.0,
          25.0,
          26.0,
          27.0
        ],
        "temperature_2m_min": [
          15.0,
          17.0,
          18.0,
          19.0,
          20.0,
          21.0,
          22.0
        ]
      }
    }
  },
  {
    "name": "London",
    "country": "United Kingdom",
    "latitude": 52.50,
    "longitude": -0.125,
    "forecasts": {
      "daily": {
        "time": [
          "2023-01-01",
          "2023-01-02",
          "2023-01-03",
          "2023-01-04",
          "2023-01-05",
          "2023-01-06",
          "2023-01-07"
        ],
        "temperature_2m_max": [
          20.0,
          22.0,
          23.0,
          24.0,
          25.0,
          26.0,
          27.0
        ],
        "temperature_2m_min": [
          15.0,
          17.0,
          18.0,
          19.0,
          20.0,
          21.0,
          22.0
        ]
      }
    },
    "historical_weather": {
      "daily": {
        "time": [
          "2022-01-01",
          "2022-01-02",
          "2022-01-03",
          "2022-01-04",
          "2022-01-05",
          "2022-01-06",
          "2022-01-07",
        ],
        "temperature_2m_max": [
          20.0,
          22.0,
          23.0,
          24.0,
          25.0,
          26.0,
          27.0
        ],
        "temperature_2m_min": [
          15.0,
          17.0,
          18.0,
          19.0,
          20.0,
          21.0,
          22.0
        ]
      }
    }
  }
]
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