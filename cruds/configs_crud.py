from ._base_crud import BaseCrud
from schemas import ConfigsSchema


class ConfigsCrud(BaseCrud[ConfigsSchema]):
    SK_MARKER = "configs"
    model = ConfigsSchema
    