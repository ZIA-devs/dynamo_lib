from ...core.enums import MessageOrigin
from pydantic import BaseModel, Field, field_validator
from typing import Optional


class BiLogsSchema(BaseModel):
    id: int = Field(default=0, alias="id")
    phone_id: int = Field(..., alias="phone_id")
    client_id: str = Field(..., alias="client_id")
    sender: str = Field(..., alias="sender")
    appointed: bool = Field(..., alias="appointed")
    canceled: bool = Field(..., alias="canceled")
    created_at: str = Field(..., alias="created_at")
    tokens: Optional[int] = Field(None, alias="tokens")
    origin: Optional[str] = Field(None, alias="origin")

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
    phone_id: Optional[int] = Field(None, alias="phone_id")
    is_total: bool = Field(False, alias="is_total")
    day: Optional[str] = Field(None, alias="day")
    total: int = Field(..., alias="total")
    appointed_count: int = Field(..., alias="appointed_count")
    canceled_count: int = Field(..., alias="canceled_count")
    user_count: int = Field(..., alias="user_count")
    assistant_count: int = Field(..., alias="assistant_count")
    clients_count: int = Field(..., alias="clients_count")
    tokens: Optional[float] = Field(None, alias="tokens")
    meta_wpp: int = Field(0, alias="meta_wpp")
    evo_wpp: int = Field(0, alias="evo_wpp")
    uazapi_wpp: int = Field(0, alias="uazapi_wpp")
    olx: int = Field(0, alias="olx")
