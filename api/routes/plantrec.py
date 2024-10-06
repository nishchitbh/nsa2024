from fastapi import status, APIRouter
from ..schema import Weather
from deeplearning import crop_recommender

route = APIRouter(tags=['Crop Recommendation'])


@route.post("/plantrec", status_code=status.HTTP_200_OK)
def recommendation(localdata: Weather):
    N = localdata.N
    P = localdata.P
    K = localdata.K
    temperature = localdata.temperature
    humidity = localdata.humidity
    ph = 7
    rainfall = 230
    recommendation = crop_recommender.predict([N, P, K, temperature, humidity, ph, rainfall])
    return {"recommendation": recommendation}
