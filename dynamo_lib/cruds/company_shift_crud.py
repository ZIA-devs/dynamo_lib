from ._base_crud import BaseCrud
from schemas import CompanyShiftSchema


class CompanyShiftCrud(BaseCrud[CompanyShiftSchema]):
    SK_MARKER = "company_shift"
    model = CompanyShiftSchema
    