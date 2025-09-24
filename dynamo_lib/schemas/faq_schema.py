from pydantic import BaseModel, Field
from typing import List, Optional


class FaqSchema(BaseModel):
    id: int = Field(default=0, alias="faq_id")
    question: str = Field(default="", alias="faq_question")
    response: str = Field(default="", alias="faq_response")
    alternative_questions: Optional[List] = Field(
        default=None, alias="faq_alternative_questions"
    )
