from ..schemas import FormSchema
from ._base_crud import BaseCrud


class FormsCrud(BaseCrud[FormSchema]):
    SK_MARKER = "form"
    model = FormSchema
