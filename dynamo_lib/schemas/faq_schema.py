from pydantic import BaseModel, Field


class FaqSchema(BaseModel):
    id: int = Field(default=0, alias="faq_id", description="ID of the FAQ entry")

    question: str = Field(
        default="", alias="faq_question", description="Question in the FAQ entry"
    )

    response: str = Field(
        default="", alias="faq_response", description="Response to the FAQ entry"
    )
