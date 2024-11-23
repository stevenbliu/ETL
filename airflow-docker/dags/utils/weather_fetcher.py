import requests

def fetch_weather_data():
    API_KEY = "962dd890a5c714c9d46c1bd51f1ed384"
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
