import os

import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.lib.ssh import (
    CatfordCastleMiniSSHClient,
    CatfordCastleSSHClient,
    SussexMewsSSHClient,
)
from app.models.kitchen_dashboard import KitchenDashboardUpdateRequest


router = APIRouter(
    prefix="/kitchen-dashboard",
    tags=["kitchen-dashboard"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def hello():
    return {"message": "Hello from Kitchen Dashboard!"}


@router.post("/update")
async def update_dashboard(update_request: KitchenDashboardUpdateRequest):
    ssh_client: SussexMewsSSHClient = update_request.ssh_client()

    # update url
    update_url_command = f"echo '{update_request.url}' | sudo tee /boot/fullpageos.txt"
    ssh_client.execute(update_url_command).splitlines()[0]

    # reboot
    ssh_client.execute("sudo shutdown -r")

    return {"msg": "URL successfully updated. Dashboard will reboot in 1 minute"}
