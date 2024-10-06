from fastapi import status, APIRouter
from ..schema import Weather, Coordinates
from utils import connector

route = APIRouter(tags=['Weather data'])


@route.post("/weatherdata", status_code=status.HTTP_200_OK)
def recommendation(localdata: Coordinates):
    data = connector.local_index((localdata.lat, localdata.long))
    return data
