import requests
import ipinfo
import os
from dotenv import load_dotenv

load_dotenv()

# Replace 'your_ipinfo_access_token' with your actual IPInfo token
ipinfo_access_token = os.getenv("IPINFO_TOKEN")
owm_api_key = os.getenv("OWM_API")

# Fetch current location based on IP
def get_location():
    handler = ipinfo.getHandler(ipinfo_access_token)
    details = handler.getDetails()
    return details.latitude, details.longitude

# Fetch current weather based on latitude and longitude
def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={owm_api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Main function
if __name__ == '__main__':
    latitude, longitude = get_location()
    print(f"Current Location - Latitude: {latitude}, Longitude: {longitude}")
    
    weather_data = get_weather(latitude, longitude)
    if weather_data:
        print(f"Current weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")
    else:
        print("Failed to retrieve weather data.")
