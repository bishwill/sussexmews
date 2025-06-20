from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import select
from db.models.todo import Items

from app.dependencies.database import SessionDep


router = APIRouter(
    prefix="/todo",
    tags=["todo"],
)

@router.get("/items")
async def get_items(session: SessionDep):
    return session.scalars(select(Items).where(Items.completed_at == None)).all()

