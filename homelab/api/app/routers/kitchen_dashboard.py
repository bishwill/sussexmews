import os

import requests
from fastapi import APIRouter


router = APIRouter(
    prefix="/kitchen-dashboard",
    tags=["kitchen-dashboard"],
    responses={404: {"description": "Not found"}},
)

AIRFLOW_SESSION = requests.session()
AIRFLOW_SESSION.auth = (os.environ["AIRFLOW_USER"], os.environ["AIRFLOW_PWD"])
AIRFLOW_SESSION.headers = {"accept": "application/json"}


@router.get("/")
async def hello():
    return {"message": "Hello from Kitchen Dashboard!"}


@router.post("/update")
async def update_dashboard():
    response = AIRFLOW_SESSION.post(
        "https://airflow.sussexmews.co.uk/api/v1/dags/bills_history_tracker/dagRuns",
        json={},
    )
    response.raise_for_status()

    return {"message": f"Dashboard Updated!"}
