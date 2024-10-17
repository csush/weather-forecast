# Holiday Planner

An API that takes as input a list of destinations and a start and an end date. It returns a list of weather forecasts for each destination for the next 7 days, and the historical weather from 1 year before the start date to the end date.

## Developer Notes

- This is a basic API server built using Django Rest Framework. The API is defined in the `weather_forecast/api/v1/views.py` file.
- The API is tested using pytest. The tests are defined in the `weather_forecast/tests` directory.
  - The tests are quite simple, and right now they only test the services (geocoding, forecasting, and historical weather) by mocking the HTTP requests.
- I'm satisfied by how I've set up services and models. I like the ease of data transformations and the separation of concerns.
- Error handling is not robust, only catches the basic exceptions.
- Validations for external request to APIs and their responses are not complete.
- The API is not secured.
- Using serializers and viewsets seems a bit of an overkill for this project (but its good practice for me). Regardless, I think the viewset and serializers can be more structured.
- Right now it has basic formatting, but would like to add pre-commit hooks for linting and formatting.
- From a product POV:
  - It gives out a list of weather forecasts for a list of destinations for the next 7 days, and the historical weather from 1 year before the start date to the end date. Which is a basic way of holiday planning, and it can be improved by getting the exact schedule from city to city as opposed to getting the weather info for all cities on all days.
  - Due to limitation of Open Meteo API, it only gives out the weather forecast for the next 16 days, however for the sake of simplicity, I set the forecasting days to 7.
  - It fetches temperature_max and temperature_min data points. Other data points can be added if needed.

## Running the application

To run the application, run the following command:

```bash
docker compose up
```

To run the sample_request.py script, install python uv (https://docs.astral.sh/uv/) for python version management, dependency management, and virtual environment. Then, run the following command (while the compose is up):

```bash
uv run python sample_request.py
```

## API

### GET [/api/v1/plan](http://localhost:8000/api/v1/plan/)

#### Body

- `destinations`: A list of destinations to get weather forecasts for.
- `start_date`: A string representing the start date in the format `YYYY-MM-DD`.
- `end_date`: A string representing the end date in the format `YYYY-MM-DD`.
- Example:
```json
{
	"destinations": ["Berlin", "Valencia"],
	"start_date": "2024-10-17",
	"end_date": "2024-10-27"
}
```

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

To run the tests, install python uv (https://docs.astral.sh/uv/) if you haven't already.
Then, run the following command:
```bash
uv run make test
```
