from ..schemas import CompanyShiftSchema
from ._base_crud import BaseCrud


class CompanyShiftCrud(BaseCrud[CompanyShiftSchema]):
    SK_MARKER = "company_shift"
    model = CompanyShiftSchema
    