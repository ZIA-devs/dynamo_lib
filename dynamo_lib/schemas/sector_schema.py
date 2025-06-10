from ..core.enums import SectorStatus
from pydantic import BaseModel, Field


class SectorSchema(BaseModel):
    id: int = Field(default=0, alias="sector_id", description="ID of the sector")

    name: str = Field(default="", alias="sector_name", description="Name of the sector")

    phone: str = Field(
        default="", alias="sector_phone", description="Phone number of the sector"
    )

    user: str = Field(
        default="", alias="sector_user", description="User responsible for the sector"
    )

    send_contact: bool = Field(
        default=False,
        alias="sector_send_contact",
        description="Whether to send contact information",
    )

    status: SectorStatus = Field(
        default=SectorStatus.IDLE,
        alias="sector_status",
        description="Status of the sector",
    )

    client_phone: str = Field(
        default="",
        alias="sector_client_phone",
        description="Phone number of the client in the sector",
    )
