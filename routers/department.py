from fastapi import APIRouter, Query
import httpx
from utils.response import full_success_response, fail_success_response

router = APIRouter()

@router.get("/api/department/")
async def get_department_info(name: str = Query(..., description="Nombre del departamento")):
    url = f"https://api-colombia.com/api/v1/Department/name/{name}"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            department_data = response.json()
        
        if department_data:
            department_info = {
                "id": department_data[0]["id"],
                "name": department_data[0]["name"]
            }
            return full_success_response(data=department_info, count=1)
        else:
            return fail_success_response(message="Department not found", count=0)
    
    except httpx.HTTPStatusError as exc:
        return fail_success_response(message=f"Error fetching data: {exc.response.status_code}", count=0)
