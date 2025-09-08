from core.enums import MessageOrigin
from pydantic import BaseModel, Field, field_validator
from typing import Optional


class BiLogsSchema(BaseModel):
    id: int = Field(
        default=0, alias="id", description="Unique identifier for the log entry"
    )
    phone_id: int = Field(
        ...,
        alias="phone_id",
        description="Phone ID associated with the log entry",
    )
    client_id: str = Field(..., alias="client_id", description="Client identifier")
    sender: str = Field(..., alias="sender", description="Sender of the log entry")
    appointed: bool = Field(
        ...,
        alias="appointed",
        description="Indicates if the appointment was made",
    )
    canceled: bool = Field(
        ...,
        alias="canceled",
        description="Indicates if the appointment was canceled",
    )
    created_at: str = Field(
        ...,
        alias="created_at",
        description="Timestamp of when the log entry was created",
    )
    tokens: Optional[int] = Field(
        None, alias="tokens", description="Number of tokens used in the log entry"
    )
    origin: Optional[str] = Field(
        None, alias="origin", description="Origin of the message in the log entry"
    )

    @field_validator("origin", mode="before")
    def validate_origin(cls, value):
        if not isinstance(value, str):
            match value:
                case MessageOrigin.META_WPP:
                    return "meta_wpp"
                case MessageOrigin.EVO_WPP:
                    return "evo_wpp"
                case MessageOrigin.UAZAPI:
                    return "uazapi_wpp"
                case MessageOrigin.OLX:
                    return "olx"
                case _:
                    return None
        return value


class BiLogsOutputSchema(BaseModel):
    day: Optional[str] = Field(None, alias="day", description="Date of the log entry")
    total: int = Field(..., alias="total", description="Total number of log entries")
    appointed_count: int = Field(
        ..., alias="appointed_count", description="Count of appointed logs"
    )
    canceled_count: int = Field(
        ..., alias="canceled_count", description="Count of canceled logs"
    )
    user_count: int = Field(..., alias="user_count", description="Count users msg")
    assistant_count: int = Field(
        ..., alias="assistant_count", description="Count of assistants msg"
    )
    clients_count: int = Field(
        ..., alias="clients_count", description="Count of unique clients in logs"
    )
    tokens: Optional[float] = Field(
        None, alias="tokens", description="Number of tokens used in the log entry"
    )
    meta_wpp: int = Field(
        0, alias="meta_wpp", description="Count of messages from Meta WhatsApp"
    )
    evo_wpp: int = Field(
        0, alias="evo_wpp", description="Count of messages from Evo WhatsApp"
    )
    uazapi_wpp: int = Field(
        0, alias="uazapi_wpp", description="Count of messages from UAZAPI WhatsApp"
    )
    olx: int = Field(0, alias="olx", description="Count of messages from OLX")
