from fastapi import APIRouter


router = APIRouter(
    prefix="/kitchen-dashboard",
    tags=["kitchen-dashboard"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def hello():
    return {"message": "Hello from Kitchen Dashboard!"}
