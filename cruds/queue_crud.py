from ._base_crud import BaseCrud
from schemas import QueueSchema


class QueueCrud(BaseCrud[QueueSchema]):
    SK_MARKER = "queue#"
    model = QueueSchema

    @classmethod
    def create(cls, phone_id:str, sector_id:int, sector_name:str, client_phone:str, timestamp:str) -> QueueSchema:
        data = {
            "queue_client_phone": sector_id,
            "queue_sector_id": client_phone,
            "sector_name": sector_name,
        }
        company_sk = cls.SK_MARKER + str(sector_id) + '#' + client_phone + '#' + timestamp
        return super().add(pk=phone_id, sk=company_sk, data=data)