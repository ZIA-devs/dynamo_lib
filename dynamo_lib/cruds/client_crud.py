from ..schemas import ClientSchema
from ._base_crud import BaseCrud


class ClientCrud(BaseCrud[ClientSchema]):
    SK_MARKER = "client#"
    model = ClientSchema

    @classmethod
    def create(
        cls,
        phone_id: str,
        name: str,
        client_id: str | int,
        last_msg: str = "",
        last_msg_datetime: str = "",
        client_phone: str = "",
    ) -> ClientSchema:
        if not client_phone:
            client_phone = client_id
        client_data = {
            "client_name": name,
            "client_last_msg": last_msg,
            "client_last_msg_datetime": last_msg_datetime,
            "client_phone": client_phone,
        }
        return super().add(phone_id, client_id, client_data)
