# complex_source.py
# A more advanced Python script demonstrating API calls, error handling, and data processing

import requests
import json
from datetime import datetime

class WeatherFetcher:
    """Fetches weather data from a public API and processes it."""

    def __init__(self, city: str, api_key: str):
        self.city = city
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self):
        try:
            response = requests.get(
                self.base_url,
                params={"q": self.city, "appid": self.api_key, "units": "metric"}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather: {e}")
            return None

    def display_weather(self, data):
        if not data:
            print("No weather data available.")
            return
        city = data.get("name")
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        print(f"Weather in {city}: {temp}°C, {condition}")

        # Save to file
        with open("weather_log.json", "a") as f:
            log_entry = {
                "city": city,
                "temp": temp,
                "condition": condition,
                "timestamp": datetime.now().isoformat()
            }
            f.write(json.dumps(log_entry) + "\n")

if __name__ == "__main__":
    # Replace with your own OpenWeatherMap API key
    API_KEY = "YOUR_API_KEY"
    fetcher = WeatherFetcher("Mysuru", API_KEY)
    weather_data = fetcher.fetch_weather()
    fetcher.display_weather(weather_data)
