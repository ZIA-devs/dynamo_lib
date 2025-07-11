from ..core.enums import MessageTemplateHeaderType
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional


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
        alias="send_off_language",
        description="Language of the send_off template",
    )

    category: str = Field(
        default="MARKETING",
        alias="send_off_category",
        description="Category of the send_off template",
    )

    body: str = Field(
        alias="send_off_body",
        description="Body of the send_off template",
    )

    header_type: MessageTemplateHeaderType = Field(
        default=MessageTemplateHeaderType.NONE,
        alias="send_off_header_type",
        description="Header type of the send_off template",
    )

    header: str = Field(
        default="",
        alias="send_off_header",
        description="Header of the send_off template",
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

    var_examples: Optional[Dict[str, Any]] = Field(
        default=None,
        alias="send_off_var_examples",
        description="Examples of the send_off template",
    )

    parameter_format: str = Field(
        default="NAMED",
        alias="send_off_parameter_format",
        description="Parameter format of the send_off template",
    )

    edit_timestamp: int = Field(
        default=0,
        alias="send_off_edit_timestamp",
        description="Timestamp of the last edit of the send_off template",
    )
