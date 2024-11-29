from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), "../../.env")

# Load .env file
load_result = load_dotenv(dotenv_path)
print('.env Load Result:', load_result)

# Access secrets
OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
print('API_KEY:', OPEN_WEATHER_API_KEY)
# database_url = os.getenv("DATABASE_URL")

# print(f"API Key: {api_key}")
# print(f"Database URL: {database_url}")


import requests

def fetch_weather_data(API_KEY=OPEN_WEATHER_API_KEY):
    # API_KEY = OPEN_WEATHER_API_KEY
    CITY = "San Francisco"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {"q": CITY, "appid": API_KEY, "units": "imperial"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Temp: {data['main']['temp']}°F, Desc: {data['weather'][0]['description']}")
    else:
        print(f"Error: {response.status_code}")

fetch_weather_data()
