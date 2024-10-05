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
url = f"https://api.nasa.gov/planetary/earth/imagery?lon={details.longitude}&lat={details.latitude}&dim=0.7&api_key={os.getenv('NASA_API')}"
response = requests.get(url)
print(url)
# print(response.text)
# print(response.content)
with open("output_image.png", "wb") as file:
    file.write(response.content)