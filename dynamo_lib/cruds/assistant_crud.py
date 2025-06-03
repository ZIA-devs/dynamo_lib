from ._base_crud import BaseCrud
from schemas import AssistantSchema


class AssistantCrud(BaseCrud[AssistantSchema]):
    SK_MARKER = "assistant"
    model = AssistantSchema
    