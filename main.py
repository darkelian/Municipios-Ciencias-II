from fastapi import FastAPI
from routers import department, city

app = FastAPI()

app.include_router(department.router)
app.include_router(city.router)