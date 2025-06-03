from ..schemas.sector_schema import SectorSchema
from ._base_crud import BaseCrud


class SectorCrud(BaseCrud[SectorSchema]):
    SK_MARKER = "sector#"
    model = SectorSchema

    @classmethod
    def create(cls, phone_id: str, nome:str, telefone:str, user:str, send_contact:bool) -> SectorSchema:
        sector ={
            'sector_name': nome,
            'sector_phone': telefone,
            'sector_user': user,
            'sector_send_contact': send_contact,
        }
        return cls.add_with_id(pk=phone_id, data=sector, id_key='sector_id')
