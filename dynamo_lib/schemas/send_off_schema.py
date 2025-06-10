from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SendOffSchema(BaseModel):
    id: int = Field(
        alias="send_off_id",
        description="ID of the send_off template",
    )

    name: str = Field(
        alias="send_off_name", description="Name of the send_off template"
    )

    language: str = Field(
        default="pt_BR",
        alias="send_off_message",
        description="Language of the send_off template",
    )

    category: str = Field(
        default="UTILITY",
        alias="send_off_category",
        description="Category of the send_off template",
    )

    header_image: str = Field(
        default="",
        alias="send_off_header_image",
        description="Header image of the send_off template",
    )

    header_text: str = Field(
        default="",
        alias="send_off_header_text",
        description="Header text of the send_off template",
    )

    body_text: str = Field(
        alias="send_off_body_text",
        description="Body text of the send_off template",
    )

    var_examples: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        alias="send_off_var_examples",
        description="Variable examples of the send_off template",
    )

    parameter_format: str = Field(
        default="NAMED",
        alias="send_off_parameter_format",
        description="Parameter format of the send_off template",
    )
