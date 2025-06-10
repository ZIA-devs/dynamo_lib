from pydantic import BaseModel, Field


class ReengagementSchema(BaseModel):
    message: str = Field(
        default="", alias="reengagement_message", description="Reengagement message"
    )

    wait_time: int = Field(
        default=30,
        alias="reengagement_wait_time",
        description="Wait time for reengagement in minutes",
    )
