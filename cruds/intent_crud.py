from ._base_crud import BaseCrud
from schemas import IntentSchema


class IntentCrud(BaseCrud[IntentSchema]):
    TABLE_NAME = "Intents"
    model = IntentSchema
