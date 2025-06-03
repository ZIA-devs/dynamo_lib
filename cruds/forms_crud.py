from ._base_crud import BaseCrud
from schemas import FormSchema


class FormsCrud(BaseCrud[FormSchema]):
    SK_MARKER = "form"
    model = FormSchema