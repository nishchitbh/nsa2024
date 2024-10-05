import requests
import os
from dotenv import load_dotenv
import ipinfo
from datetime import datetime


load_dotenv()

# Define your API key and base URL
API_KEY = os.getenv("OWM_API")
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'

# Specify the city you want to fetch forecast data for
city = 'Kathmandu'

# Construct the complete URL
url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'

# Make the API request
response = requests.get(url)

# Parse the JSON data
data = response.json()

# Check if the request was successful
if response.status_code == 200:
    # Extract and print forecast data for each 3-hour interval
    print(f"Weather forecast for {city}:\n")
    
    for forecast in data['list']:
        # Get the date and time for each forecast
        dt = datetime.fromtimestamp(forecast['dt'])
        temperature = forecast['main']['temp']
        weather_desc = forecast['weather'][0]['description']
        
        print(f"Date & Time: {dt}")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather_desc}")
        print('-' * 40)
else:
    print(f"Error {response.status_code}: {data['message']}")
