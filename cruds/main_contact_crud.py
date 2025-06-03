from ._base_crud import BaseCrud
from schemas import MainContactSchema


class MainContactCrud(BaseCrud[MainContactSchema]):
    SK_MARKER = "main_contact"
    model = MainContactSchema
