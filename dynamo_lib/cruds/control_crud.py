from ..core.enums import EmpresaPlan, ControlStatus
from ..schemas import ControlSchema
from ._base_crud import BaseCrud


class ControlCrud(BaseCrud[ControlSchema]):
    TABLE_NAME = "Control"
    model = ControlSchema
    
    @classmethod
    def create(cls, company_identification:str, plan:EmpresaPlan, token_openai:str, employee_limit:int) -> ControlSchema:
        new_control = {
            'plan': plan,
            'token_openai': token_openai,
            'employee_limit': employee_limit,
            'status': ControlStatus.NEED_META_LOGIN
        }
        return super().add(pk=company_identification, sk="", data=new_control)
