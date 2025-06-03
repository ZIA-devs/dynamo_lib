from ..schemas import MainContactSchema
from ._base_crud import BaseCrud


class MainContactCrud(BaseCrud[MainContactSchema]):
    SK_MARKER = "main_contact"
    model = MainContactSchema
