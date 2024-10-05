import ipinfo
from dotenv import load_dotenv
import os
import requests

load_dotenv()


# Replace 'your_token' with your actual token from ipinfo.io
access_token = os.getenv("IPINFO_TOKEN")
handler = ipinfo.getHandler(access_token)

# Get info based on IP
details = handler.getDetails()

print(f"Latitude: {details.latitude}, Longitude: {details.longitude}")

response = requests.get(f"https://soil.narc.gov.np/api/soildata?lat={details.latitude}&lon={details.longitude}")
print(response.content)