# integrations/weather_api.py
import requests
import os

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "your-api-key")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):
    """
    কোনো শহরের বর্তমান আবহাওয়া পান
    """
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].title(),
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
            print(f"🌤️ Weather in {city}: {weather['temperature']}°C, {weather['description']}")
            return weather
        else:
            print(f"❌ Weather API Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return None

# টেস্ট
if __name__ == "__main__":
    get_weather("Paris")
