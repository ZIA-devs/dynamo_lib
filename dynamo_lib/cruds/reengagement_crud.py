from ._base_crud import BaseCrud
from schemas.reengagement_schema import ReengagementSchema


class ReengagementCrud(BaseCrud[ReengagementSchema]):
    SK_MARKER = "reengagement"
    model = ReengagementSchema

    @classmethod
    def create(cls, phone_id: str, mensagem: str, wait_time: int) -> ReengagementSchema:
        reengagement = {
            "reengagement_message": mensagem,
            "reengagement_wait_time": wait_time
        }
        return cls.add(pk=phone_id, sk="", data=reengagement)
