from pydantic import BaseModel, Field, field_validator
from ..core.enums import MessageOrigin


class LogsSchema(BaseModel):
    company_id: int = Field(default=0, alias="company_id")
    logs_sk: str = Field(default="", alias="sk")
    client_id: str | int = Field(default="", alias="client_id")
    message: str = Field(default="", alias="message")
    sender: str = Field(default="", alias="sender")
    type: str = Field(default="", alias="type")
    time: str = Field(default="", alias="time")
    ttl: int = Field(default=0, alias="ttl")
    message_origin: MessageOrigin = Field(
        default=MessageOrigin.META_WPP, alias="message_origin"
    )

    @field_validator("client_id", mode="after")
    @classmethod
    def convert_client_it_to_str(cls, v: str | int) -> str:
        return str(v) if isinstance(v, int) else v
