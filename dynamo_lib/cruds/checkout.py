from ..schemas import CheckoutSchema
from ._base_crud import BaseCrud


class CheckoutCrud(BaseCrud[CheckoutSchema]):
    TABLE_NAME = "Checkout"
    model = CheckoutSchema
