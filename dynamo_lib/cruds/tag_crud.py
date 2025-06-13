from ..schemas import TagSchema
from ._base_crud import BaseCrud
from typing import Dict, Any


class TagCrud(BaseCrud[TagSchema]):
    SK_MARKER = "tag#"
    model = TagSchema

    @classmethod
    def create(cls, phone_id: str, name: str, color: str) -> TagSchema:

        data: Dict[str, Any] = {
            "tag_name": name,
            "tag_color": color,
        }

        return cls.add_with_id(pk=phone_id, data=data, id_key="tag_id")
