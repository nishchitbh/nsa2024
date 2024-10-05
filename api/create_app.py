from fastapi import FastAPI
from .routes import mainpage


app = FastAPI()

app.include_router(mainpage.route)

