import meteomatics.api as api
from datetime import datetime, timedelta
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Meteomatics API credentials
username = os.getenv("METEOUSER")
password = os.getenv("METEOPW")
# Set up the request parameters
def local_index(coordinate):
    coordinates = [coordinate]  # Zurich, Switzerland (latitude, longitude)
    now = datetime.utcnow()
    startdate = now - timedelta(days=60)
    enddate = now
    interval = timedelta(days=1)

    # Parameters to retrieve
    parameters = [
        'soil_moisture_index_-10cm:idx',  # Soil moisture in the top 10cm
        'drought_index:idx',  # Drought index
        't_2m:C',  # Temperature at 2 meters above ground in Celsius
        'evapotranspiration_1h:mm',  # Evapotranspiration in the last hour in millimeters
        'precip_1h:mm'  # Rainfall in the last hour in millimeters
    ]

    try:
        # Make the API request
        df = api.query_time_series(
            coordinate_list=coordinates,
            parameters=parameters,
            startdate=startdate,
            enddate=enddate,
            interval=interval,
            username=username,
            password=password
        )

        # Print the lists
        json_data = {
            "soil_moisture_index": df["soil_moisture_index_-10cm:idx"].tolist(),
            "drought_index": df["drought_index:idx"].tolist(),
            "temperature": df["t_2m:C"].tolist(),
            "evapotranspiration": df["evapotranspiration_1h:mm"].tolist(),
            "rainfall": df["precip_1h:mm"].tolist()
        }
        # The returned DataFrame is already in the desired format
        return json_data

    except api.APIException as e:
        return f"Error: {e}"

