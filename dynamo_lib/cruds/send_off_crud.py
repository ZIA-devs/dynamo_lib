from ..schemas import SendOffSchema
from ..core.enums import SendOffHeaderType
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
        body: str,
        header_type: SendOffHeaderType = SendOffHeaderType.NONE,
        header: str = "",
        footer: str = "",
        buttons: Optional[List[Dict[str, Any]]] = None,
    ) -> SendOffSchema:

        data: Dict[str, Any] = {
            "send_off_id": id,
            "send_off_name": name,
            "send_off_body": body,
        }

        if header_type != SendOffHeaderType.NONE:
            data["send_off_header"] = header

        if footer:
            data["send_off_footer"] = footer

        if buttons:
            data["send_off_buttons"] = buttons

        return cls.add(pk=phone_id, sk=f"{cls.SK_MARKER}{id}", data=data)
