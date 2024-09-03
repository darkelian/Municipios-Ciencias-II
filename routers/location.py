import httpx
from fastapi import APIRouter, HTTPException, Query
from utils.response import full_success_response, fail_success_response

router = APIRouter()

@router.get("/api/location")
async def get_location_info(place: str = Query(..., description="Nombre del lugar")):
    # Paso 1: Obtener latitud y longitud con PositionStack (u otra API)
    geocode_url = f"http://api.positionstack.com/v1/forward?access_key=cc588117ccc010dcf6b8e19c8e71f12f&query={place}"
    
    try:
        async with httpx.AsyncClient() as client:
            # Primera solicitud: Obtener latitud y longitud
            geocode_response = await client.get(geocode_url)
            geocode_response.raise_for_status()
            geocode_data = geocode_response.json()
        
            if geocode_data and geocode_data['data']:
                result = geocode_data['data'][0]
                latitude = result['latitude']
                longitude = result['longitude']

                # Segunda solicitud: Obtener altitud con Open-Elevation
                elevation_url = f"https://api.open-elevation.com/api/v1/lookup?locations={latitude},{longitude}"
                elevation_response = await client.get(elevation_url)
                elevation_response.raise_for_status()
                elevation_data = elevation_response.json()

                if elevation_data and elevation_data['results']:
                    altitude = elevation_data['results'][0]['elevation']

                    location_info = {
                        "latitude": latitude,
                        "longitude": longitude,
                        "altitude": altitude
                    }
                    return full_success_response(data=location_info, count=1)

                else:
                    return fail_success_response(message="Elevation data not found", count=0)

            else:
                return fail_success_response(message="Location not found", count=0)
    
    except httpx.HTTPStatusError as exc:
        return fail_success_response(message=f"Error fetching data: {exc.response.status_code}", count=0)
