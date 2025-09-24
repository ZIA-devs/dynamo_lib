from ..core.enums import ClientStatus
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional


class ClientSchema(BaseModel):
    id: str = Field(alias="company_sk")
    last_msg: str = Field(default="", alias="client_last_msg")
    last_msg_datetime: str = Field(default="", alias="client_last_msg_datetime")
    name: str = Field(default="", alias="client_name")
    phone: str = Field(default="", alias="client_phone")
    sector_phone: str = Field(default="", alias="client_sector_phone")
    status: ClientStatus = Field(default=ClientStatus.ON_BOT, alias="client_status")
    thread: Optional[str] = Field(default="", alias="client_thread")
    tags: List[str] = Field(default_factory=list, alias="client_tags")
    has_made_appointment: bool = Field(
        default=False, alias="client_has_made_appointment"
    )
    msg_count: int = Field(default=0, alias="client_msg_count")
    msg_count_wpp: int = Field(default=0, alias="client_msg_count_wpp")
    msg_count_olx: int = Field(default=0, alias="client_msg_count_olx")

    @field_validator("id", mode="before")
    def validate_id(cls, value):
        return str(value).split("#", 1)[-1]
