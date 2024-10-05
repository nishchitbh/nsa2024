from fastapi import FastAPI
from .routes import mainpage, plantrec


app = FastAPI()

app.include_router(mainpage.route)
app.include_router(plantrec.route)
