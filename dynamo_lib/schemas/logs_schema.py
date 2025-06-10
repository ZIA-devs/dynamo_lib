from pydantic import BaseModel, Field, field_validator


class LogsSchema(BaseModel):
    company_id: int = Field(
        default=0, alias="company_id", description="ID of the company"
    )

    logs_sk: str = Field(
        default="", alias="sk", description="Unique identifier for the log entry"
    )

    client_id: str | int = Field(
        default="", alias="client_id", description="ID of the client"
    )

    message: str = Field(
        default="", alias="message", description="Message in the log entry"
    )

    sender: str = Field(
        default="", alias="sender", description="Sender of the message in the log entry"
    )

    type: str = Field(
        default="", alias="type", description="Type of the message in the log entry"
    )

    time: str = Field(
        default="", alias="time", description="Timestamp of the log entry"
    )

    ttl: int = Field(
        default=0, alias="ttl", description="Time to live for the log entry"
    )

    @field_validator("client_id", mode="after")
    @classmethod
    def convert_client_it_to_str(cls, v: str | int) -> str:
        return str(v) if isinstance(v, int) else v
