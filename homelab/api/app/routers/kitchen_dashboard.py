from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.lib.ssh import (
    SussexMewsSSHClient,
)
from app.models.kitchen_dashboard import (
    KitchenDashboardUpdateRequest,
    KitchenDashboardShutdownRequest,
    KitchenDashboardRebootRequest,
)


router = APIRouter(
    prefix="/kitchen-dashboard",
    tags=["kitchen-dashboard"],
    responses={404: {"description": "Not found"}},
)


@router.post("/update")
async def update_dashboard(update_request: KitchenDashboardUpdateRequest):
    ssh_client: SussexMewsSSHClient = update_request.ssh_client()

    # update url
    update_url_command = f"echo '{update_request.url}' | sudo tee /boot/fullpageos.txt"
    ssh_client.execute(update_url_command).splitlines()[0]

    # reboot
    ssh_client.execute("sudo reboot -h now")

    return JSONResponse(content={"msg": "URL successfully updated!"})


@router.post("/shutdown")
async def shutdown_dashboard(shutdown_request: KitchenDashboardShutdownRequest):
    shutdown_request.ssh_client().execute("sudo shutdown -h now")

    return JSONResponse(
        content={
            "msg": f"{shutdown_request.screen.capitalize()} screen successfullly shutdown!"
        }
    )


@router.post("/reboot")
async def reboot_dashboard(reboot_request: KitchenDashboardRebootRequest):
    reboot_request.ssh_client().execute("sudo reboot -h now")

    return JSONResponse(
        content={
            "msg": f"{reboot_request.screen.capitalize()} screen successfullly rebooted!"
        }
    )
