from pydantic import BaseModel


class Weather(BaseModel):
    N: int
    P: int
    K: int
    temperature: float
    humidity: float
