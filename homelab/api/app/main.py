from fastapi import FastAPI

from .routers import kitchen_dashboard


app = FastAPI(title="Sussex Mews Rest API", version="0.1.1")


app.include_router(kitchen_dashboard.router)
