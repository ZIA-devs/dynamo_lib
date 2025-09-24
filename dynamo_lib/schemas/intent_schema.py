from pydantic import BaseModel, Field


class IntentSchema(BaseModel):
    intent: str = Field(default="", alias="intent")
    file_search: bool = Field(default=False, alias="file_search")
    function: str = Field(default="", alias="function")
    instruction: str = Field(default="", alias="instruction")
    start_reengagement: bool = Field(default=False, alias="start_reengagement")
    stop_reengagement: bool = Field(default=False, alias="stop_reengagement")
