from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
)



@router.get("/items")
async def get_items():
    
    return JSONResponse(
        content={"msg": "items"}
    )
