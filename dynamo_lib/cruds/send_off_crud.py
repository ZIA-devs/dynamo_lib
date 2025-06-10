from ..schemas import SendOffSchema
from ._base_crud import BaseCrud
from typing import Optional, Dict, Any


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
        body_text: str,
        header_image: str = "",
        header_text: str = "",
        var_examples: Optional[Dict[str, Any]] = None,
        parameter_format: str = "NAMED",
    ) -> SendOffSchema:

        data: Dict[str, Any] = {
            "send_off_id": id,
            "send_off_name": name,
            "send_off_language": language,
            "send_off_category": category,
            "send_off_body_text": body_text,
        }

        if header_image:
            data["send_off_header_image"] = header_image

        if header_text:
            data["send_off_header_text"] = header_text

        if var_examples:
            data["send_off_var_examples"] = var_examples
            data["send_off_parameter_format"] = parameter_format

        return cls.add(pk=phone_id, sk=f"{cls.SK_MARKER}{id}", data=data)
