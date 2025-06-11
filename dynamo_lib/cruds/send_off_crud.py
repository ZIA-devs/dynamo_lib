from ..schemas import SendOffSchema
from ..core.enums import MessageTemplateHeaderType
from ._base_crud import BaseCrud
from typing import List, Dict, Any, Optional


class SendOffCrud(BaseCrud[SendOffSchema]):
    SK_MARKER = "send_off#"
    model = SendOffSchema

    @classmethod
    def create(
        cls,
        phone_id: str,
        id: int,
        name: str,
        language: str,
        category: str,
        body: str,
        header_type: MessageTemplateHeaderType = MessageTemplateHeaderType.NONE,
        header: str = "",
        footer: str = "",
        buttons: Optional[List[Dict[str, Any]]] = None,
        var_examples: Optional[Dict[str, Any]] = None,
        parameter_format: str = "NAMED",
    ) -> SendOffSchema:

        data: Dict[str, Any] = {
            "send_off_id": id,
            "send_off_name": name,
            "send_off_language": language,
            "send_off_category": category,
            "send_off_body": body,
        }

        if header_type != MessageTemplateHeaderType.NONE and header:
            data["send_off_header_type"] = header_type.value
            data["send_off_header"] = header

        if footer:
            data["send_off_footer"] = footer

        if buttons:
            data["send_off_buttons"] = buttons

        if var_examples:
            data["send_off_var_examples"] = var_examples
            data["send_off_parameter_format"] = parameter_format

        return cls.add(pk=phone_id, sk=f"{cls.SK_MARKER}{id}", data=data)
