import datetime as dt
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import select
from db.models.todo import Items

from app.dependencies.database import SessionDep
from app.models.todo import (
    CreateTaskRequest,
    CreateTaskResponse,
    CompleteTaskRequest,
    CompleteTasksRequest,
)

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
)


@router.get("/tasks")
async def get_all_tasks(session: SessionDep):
    return session.scalars(select(Items)).all()


@router.get("/tasks/complete")
async def get_all_completed_tasks(session: SessionDep):
    return session.scalars(select(Items).where(Items.completed_at.is_(None))).all()


@router.get("/tasks/incomplete")
async def get_all_incomplete_items(session: SessionDep):
    return session.scalars(select(Items).where(Items.completed_at.is_(None))).all()


@router.get("/task")
async def get_item(id: int, session: SessionDep):
    return session.scalars(select(Items).where(Items.id == id)).all()


@router.post("/task")
async def create_task(create_task_request: CreateTaskRequest, session: SessionDep):
    task = Items(
        task=create_task_request.description,
        created_at=dt.datetime.now(tz=dt.timezone.utc),
        created_by=create_task_request.username,
        updated_at=dt.datetime.now(tz=dt.timezone.utc),
        updated_by=create_task_request.username,
    )
    session.add(task)
    session.commit()
    return CreateTaskResponse(id=task.id)


@router.post("/task/complete")
async def complete_task(complete_task_request: CompleteTaskRequest, session: SessionDep):
    task = session.scalar(select(Items).where(Items.id == complete_task_request.id))

    if task is None:
        return JSONResponse(content={"msg": "Task not found."}, status_code=404)

    if task.completed_at is not None:
        return JSONResponse(content={"msg": "Task is already completed"}, status_code=200)

    now = dt.datetime.now(tz=dt.timezone.utc)
    task.completed_at = now
    task.completed_by = complete_task_request.username
    task.updated_at = now
    task.updated_by = complete_task_request.username

    session.commit()
    return JSONResponse(content={"msg": "Task updated successfully."})


@router.post("/tasks/complete")
async def complete_all_tasks(complete_tasks_request: CompleteTasksRequest, session: SessionDep):
    incomplete_tasks = session.scalars(select(Items).where(Items.completed_at.is_(None))).all()

    now = dt.datetime.now(tz=dt.timezone.utc)
    for task in incomplete_tasks:
        task.completed_at = now
        task.completed_by = complete_tasks_request.username
        task.updated_at = now
        task.updated_by = complete_tasks_request.username

    session.commit()

    return JSONResponse(content={"msg": "Tasks updated successfully."})
