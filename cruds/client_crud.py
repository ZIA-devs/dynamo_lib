from ._base_crud import BaseCrud
from schemas import ClientSchema


class ClientCrud(BaseCrud[ClientSchema]):
    SK_MARKER = "client#"
    model = ClientSchema
    