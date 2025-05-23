from enum import StrEnum

from pydantic import BaseModel

from app.lib.ssh import (
    SussexMewsSSHClient,
    CatfordCastleMiniSSHClient,
    CatfordCastleSSHClient,
)


class Screen(StrEnum):
    left = "left"
    right = "right"


class KitchenDashboardUpdateRequest(BaseModel):
    screen: Screen
    url: str

    @property
    def server_name(self) -> str:
        mapping = {
            "left": "catfordcastlemini",
            "right": "catfordcastle",
        }
        return mapping[self.screen.value]

    @property
    def ssh_client(self) -> SussexMewsSSHClient:
        mapping = {
            "catfordcastle": CatfordCastleSSHClient,
            "catfordcastlemini": CatfordCastleMiniSSHClient,
        }
        return mapping[self.server_name]
