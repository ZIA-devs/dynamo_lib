from ..core.enums import EmpresaPlan, ControlStatus, EmpresaTipo
from ..schemas import ControlSchema
from ._base_crud import BaseCrud


class ControlCrud(BaseCrud[ControlSchema]):
    TABLE_NAME = "Control"
    model = ControlSchema

    @classmethod
    def create(
        cls,
        company_identification: str,
        plan: EmpresaPlan,
        token_openai: str,
        employee_limit: int,
        is_uazapi: bool = True,
        has_olx: bool = False,
        business_type: EmpresaTipo = EmpresaTipo.PADRAO,
    ) -> ControlSchema:

        new_control = {
            "plan": plan,
            "token_openai": token_openai,
            "employee_limit": employee_limit,
            "status": ControlStatus.NEED_META_LOGIN,
            "is_uazapi": is_uazapi,
            "has_olx": has_olx,
            "business_type": business_type,
        }
        return super().add(pk=company_identification, sk="", data=new_control)
