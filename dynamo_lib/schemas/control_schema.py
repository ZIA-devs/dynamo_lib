from ..core.enums import ControlStatus, EmpresaPlan
from ..core.enums import EmpresaPlan, EmpresaTipo
from pydantic import BaseModel, Field


class ControlSchema(BaseModel):
    company_identification: str = Field(default="", alias="company_identification")
    employee_limit: int = Field(default=0, alias="employee_limit")
    phone_id: int = Field(default=0, alias="phone_id")
    token_openai: str = Field(default="", alias="token_openai")
    plan: EmpresaPlan = Field(default=EmpresaPlan.BASIC, alias="plan")
    status: ControlStatus = Field(default=ControlStatus.OKAY, alias="status")
    beta_tester: bool = Field(default=False, alias="beta_tester")
    has_send_off: bool = Field(default=False, alias="has_send_off")
    is_evolution: bool = Field(default=False, alias="is_evolution")
    is_uazapi: bool = Field(default=False, alias="is_uazapi")
    session_id: str = Field(default="0", alias="session_id")
    has_olx: bool = Field(default=False, alias="has_olx")
    business_type: EmpresaTipo = Field(
        default=EmpresaTipo.PADRAO, alias="business_type"
    )
