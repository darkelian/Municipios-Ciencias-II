
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.response import full_success_response, fail_success_response
from routers import city, location, department
from algoritm import aStar, neighbors

app = FastAPI()

# Montar la carpeta "static" para servir el index.html
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir los routers de los otros endpoints
app.include_router(city.router)
app.include_router(location.router)
app.include_router(department.router)

# Modelo para el body de la petición con las coordenadas
class Coordinates(BaseModel):
    latitude: float
    longitude: float
    altitude: float

# Endpoint para recibir coordenadas
@app.post("/api/set_location")
async def set_location(coordinates: Coordinates):
    return full_success_response({
        "latitude": coordinates.latitude,
        "longitude": coordinates.longitude,
        "altitude": coordinates.altitude
    })



ini = 'Bogotá'
goal = 'Aipe'
graph = neighbors.getGraph()
path = aStar.aStar(graph,ini,goal,neighbors.getPosition())

if path:
    print("Path found:", path)
else:
    print("No path found between", ini, "and", goal)