from fastapi import APIRouter, Query
import httpx
from utils.response import full_success_response, fail_success_response

router = APIRouter()

@router.get("/api/city/")
async def get_city_info(name: str = Query(..., description="Nombre de la ciudad")):
    url = f"https://api-colombia.com/api/v1/City/name/{name}"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            city_data = response.json()
        
        if city_data:
            city_info = {
                "id": city_data[0]["id"],
                "name": city_data[0]["name"],
                "department": city_data[0]["departmentId"]
            }
            return full_success_response(data=city_info, count=1)
        else:
            return fail_success_response(message="City not found", count=0)
    
    except httpx.HTTPStatusError as exc:
        return fail_success_response(message=f"Error fetching data: {exc.response.status_code}", count=0)
