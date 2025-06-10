from ..schemas import SendOffSchema
from ._base_crud import BaseCrud


class SectorCrud(BaseCrud[SendOffSchema]):
    SK_MARKER = "send_off#"
    model = SendOffSchema
