from fastapi import FastAPI

from .routers import kitchen_dashboard_router, todo_router


app = FastAPI(title="Sussex Mews Rest API", version="0.2.0")


app.include_router(kitchen_dashboard_router)
app.include_router(todo_router)
