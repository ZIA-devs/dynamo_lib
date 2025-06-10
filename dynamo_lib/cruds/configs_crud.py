from ..schemas import ConfigsSchema
from ._base_crud import BaseCrud


class ConfigsCrud(BaseCrud[ConfigsSchema]):
    SK_MARKER = "configs"
    model = ConfigsSchema
