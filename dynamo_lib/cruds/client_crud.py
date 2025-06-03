from ..schemas import ClientSchema
from ._base_crud import BaseCrud


class ClientCrud(BaseCrud[ClientSchema]):
    SK_MARKER = "client#"
    model = ClientSchema
    