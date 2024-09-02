from fastapi import HTTPException
from pydantic import BaseModel
from typing import Any, Optional

class ResponseModel(BaseModel):
    success: bool
    data: Optional[Any] = None
    count: Optional[int] = None
    message: Optional[str] = None

    class Config:
        # Excluir campos que son None
        orm_mode = True
        exclude_unset = True

def full_success_response(data: Any, count: int = 1) -> ResponseModel:
    return ResponseModel(success=True, data=data, count=count)

def fail_success_response(message: str, count: int = 0) -> None:
    raise HTTPException(status_code=400, detail={"success": False, "message": message, "count": count})
