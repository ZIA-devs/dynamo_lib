from ..core.enums import SectorStatus
from pydantic import BaseModel, Field


class SectorSchema(BaseModel):
    id: int = Field(default=0, alias="sector_id")
    name: str = Field(default="", alias="sector_name")
    phone: str = Field(default="", alias="sector_phone")
    user: str = Field(default="", alias="sector_user")
    send_contact: bool = Field(default=False, alias="sector_send_contact")
    status: SectorStatus = Field(default=SectorStatus.IDLE, alias="sector_status")
    client_phone: str = Field(default="", alias="sector_client_phone")
