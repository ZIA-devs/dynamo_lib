from pydantic import BaseModel, Field, field_validator


class AssistantSchema(BaseModel):
    company_description: str = Field(default="", alias="assistant_company_description")
    conversation_instruction: str = Field(
        default="", alias="assistant_conversation_instructions"
    )
    gender: str = Field(default="", alias="assistant_gender")
    name: str = Field(default="", alias="assistant_name")
    tone: str = Field(default="", alias="assistant_tone")
    use_emojis: bool = Field(default=False, alias="assistant_use_emojis")
    vector_store_id: str = Field(default="", alias="assistant_vector_store_id")
    temperature: float = Field(
        default=0.5,
        alias="assistant_temperature",
    )

    @field_validator("conversation_instruction", mode="before")
    def validate_conversation_instruction(cls, value: str | None) -> str:
        return value or ""
