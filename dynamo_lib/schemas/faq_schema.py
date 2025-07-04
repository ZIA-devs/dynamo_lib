from pydantic import BaseModel, Field
from typing import List, Optional


class FaqSchema(BaseModel):
    id: int = Field(default=0, alias="faq_id", description="ID of the FAQ entry")

    question: str = Field(
        default="", alias="faq_question", description="Question in the FAQ entry"
    )

    response: str = Field(
        default="", alias="faq_response", description="Response to the FAQ entry"
    )

    alternative_questions: Optional[List] = Field(
        default=None,
        alias="faq_alternative_questions",
        description="List of alternative questions to the FAQ entry",
    )
