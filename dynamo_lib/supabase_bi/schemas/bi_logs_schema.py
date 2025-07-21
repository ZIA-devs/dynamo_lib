from pydantic import BaseModel, Field
from datetime import datetime


class BiLogsSchema(BaseModel):
    id: int = Field(
        default=0, alias="id", description="Unique identifier for the log entry"
    )
    client_id: str = Field(
        default="", alias="client_id", description="Client identifier"
    )
    sender: str = Field(
        default=None, alias="sender", description="Sender of the log entry"
    )
    appointed: bool = Field(
        default=False,
        alias="appointed",
        description="Indicates if the appointment was made",
    )
    canceled: bool = Field(
        default=False,
        alias="canceled",
        description="Indicates if the appointment was canceled",
    )
    created_at: datetime = Field(
        default_factory=datetime.now,
        alias="created_at",
        description="Timestamp of when the log entry was created",
    )
