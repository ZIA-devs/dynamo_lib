from ..core.enums import ClientStatus
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional


class ClientSchema(BaseModel):
    last_msg: str = Field(
        default="", alias="client_last_msg", description="Last message from the client"
    )

    last_msg_datetime: str = Field(
        default="",
        alias="client_last_msg_datetime",
        description="Datetime of the last message from the client",
    )

    name: str = Field(default="", alias="client_name", description="Name of the client")

    phone: str = Field(
        default="", alias="client_phone", description="Phone number of the client"
    )

    sector_phone: str = Field(
        default="",
        alias="client_sector_phone",
        description="Sector phone number of the client",
    )

    status: ClientStatus = Field(
        default=ClientStatus.ON_BOT,
        alias="client_status",
        description="Status of the client",
    )

    thread: Optional[str] = Field(
        default="", alias="client_thread", description="Thread ID of the client"
    )

    tags: List[str] = Field(
        default_factory=list,
        alias="client_tags",
        description="Tags associated with the client",
    )

    has_made_appointment: bool = Field(
        default=False,
        alias="client_has_made_appointment",
        description="Indicates if the client has made an appointment",
    )
