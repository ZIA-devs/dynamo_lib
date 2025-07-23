from pydantic import BaseModel, Field


class AssistantSchema(BaseModel):
    company_description: str = Field(
        default="",
        alias="assistant_company_description",
        description="Description of the company for the assistant",
    )

    conversation_instruction: str = Field(
        default="",
        alias="assistant_conversation_instructions",
        description="Instructions for the assistant's conversation style",
    )

    gender: str = Field(
        default="", alias="assistant_gender", description="Gender of the assistant"
    )

    name: str = Field(
        default="", alias="assistant_name", description="Name of the assistant"
    )

    tone: str = Field(
        default="", alias="assistant_tone", description="Tone of the assistant"
    )

    use_emojis: bool = Field(
        default=False,
        alias="assistant_use_emojis",
        description="Whether the assistant uses emojis",
    )

    vector_store_id: str = Field(
        default="",
        alias="assistant_vector_store_id",
        description="ID of the vector store associated with the assistant",
    )
