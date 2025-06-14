from pydantic import BaseModel, Field


class IntentSchema(BaseModel):
    intent: str = Field(
        default="", alias="intent", description="Name of the intent entry"
    )

    file_search: bool = Field(
        default=False,
        alias="file_search",
        description="Whether the intent entry includes file search",
    )

    function: str = Field(
        default="",
        alias="function",
        description="Function associated with the intent entry",
    )

    instruction: str = Field(
        default="", alias="instruction", description="Instruction for the intent entry"
    )

    start_reengagement: bool = Field(
        default=False,
        alias="start_reengagement",
        description="Whether the intent entry starts a re-engagement",
    )

    stop_reengagement: bool = Field(
        default=False,
        alias="stop_reengagement",
        description="Whether the intent entry ends a re-engagement",
    )
