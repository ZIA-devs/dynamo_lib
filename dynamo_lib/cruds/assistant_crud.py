from ..schemas import AssistantSchema
from ._base_crud import BaseCrud


class AssistantCrud(BaseCrud[AssistantSchema]):
    SK_MARKER = "assistant"
    model = AssistantSchema
    