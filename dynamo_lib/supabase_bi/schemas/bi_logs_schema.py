from pydantic import BaseModel, Field
from datetime import datetime


class BiLogsSchema(BaseModel):
    id: int = Field(
        default=0, alias="id", description="Unique identifier for the log entry"
    )
    phonde_id: int = Field(
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


class BiLogsOutputSchema(BaseModel):
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
