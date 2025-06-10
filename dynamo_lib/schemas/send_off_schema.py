from ..core.enums import SendOffHeaderType
from pydantic import BaseModel, Field
from typing import List, Dict, Any


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
        default="MARKETING",
        alias="send_off_category",
        description="Category of the send_off template",
    )

    header_type: SendOffHeaderType = Field(
        default=SendOffHeaderType.NONE,
        alias="send_off_header_type",
        description="Header type of the send_off template",
    )

    header: str = Field(
        default="",
        alias="send_off_header",
        description="Header of the send_off template",
    )

    body: str = Field(
        alias="send_off_body",
        description="Body of the send_off template",
    )

    footer: str = Field(
        default="",
        alias="send_off_footer",
        description="Footer of the send_off template",
    )

    buttons: List[Dict[str, Any]] = Field(
        default_factory=list,
        alias="send_off_buttons",
        description="Buttons of the send_off template",
    )
