from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

app = FastAPI()

# Montar la carpeta "static" para servir el index.html
app.mount("/static", StaticFiles(directory="static"), name="static")

# Servicio que devuelve los datos de ubicación (Ejemplo para Bogotá)
@app.get("/api/location")
async def get_location(place: str):
    if place == "Bogota Cundinamarca":
        return JSONResponse(content={
            "success": True,
            "data": {
                "latitude": 4.91857,
                "longitude": -74.02799,
                "altitude": 2559.0
            },
            "count": 1
        })
    else:
        return JSONResponse(content={"success": False, "message": "Location not found"})
