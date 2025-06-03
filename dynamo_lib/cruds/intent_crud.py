from ..schemas import IntentSchema
from ._base_crud import BaseCrud


class IntentCrud(BaseCrud[IntentSchema]):
    TABLE_NAME = "Intents"
    model = IntentSchema
