from ..schemas import ClientSchema
from ._base_crud import BaseCrud


class ClientCrud(BaseCrud[ClientSchema]):
    SK_MARKER = "client#"
    model = ClientSchema
    
    @classmethod
    def create(cls, phone_id: str, name: str, client_id: str|int, last_message:str="") -> ClientSchema:
        client_data = {
            'client_name': name,
            'client_last_message': last_message
        }
        return super().add(phone_id, client_id, client_data)
    