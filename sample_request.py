import requests

url = "http://localhost:8000/api/v1/plan/"

payload = {
    "destinations": ["Berlin", "Valencia"],
    "start_date": "2024-10-17",
    "end_date": "2024-10-27"
}
headers = {
    "Content-Type": "application/json",
    "User-Agent": "insomnia/10.0.0"
}

response = requests.request("GET", url, json=payload, headers=headers)

print(response.text)