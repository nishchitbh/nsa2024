from pydantic import BaseModel


class Weather(BaseModel):
    N: int
    P: int
    K: int
    temperature: float
    humidity: float

class Coordinates(BaseModel):
    lat:float
    long:float