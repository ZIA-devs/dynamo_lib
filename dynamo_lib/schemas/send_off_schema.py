from ..core.enums import MessageTemplateHeaderType
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional


class SendOffSchema(BaseModel):
    id: int = Field(alias="send_off_id")
    name: str = Field(alias="send_off_name")
    language: str = Field(default="pt_BR", alias="send_off_language")
    category: str = Field(default="MARKETING", alias="send_off_category")
    body: str = Field(alias="send_off_body")
    header_type: MessageTemplateHeaderType = Field(
        default=MessageTemplateHeaderType.NONE, alias="send_off_header_type"
    )
    header: str = Field(default="", alias="send_off_header")
    footer: str = Field(default="", alias="send_off_footer")
    buttons: List[Dict[str, Any]] = Field(
        default_factory=list, alias="send_off_buttons"
    )
    var_examples: Optional[Dict[str, Any]] = Field(
        default=None, alias="send_off_var_examples"
    )
    parameter_format: str = Field(default="NAMED", alias="send_off_parameter_format")
    edit_timestamp: int = Field(default=0, alias="send_off_edit_timestamp")
