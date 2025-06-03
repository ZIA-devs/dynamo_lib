from ..core.enums import ControlStatus, EmpresaPlan 
from pydantic import BaseModel, Field


class ControlSchema(BaseModel):
    company_identification: str = Field(default='', alias='company_identification', description='Company identification')
    employee_limit: int = Field(default=0, alias='employee_limit', description='Limit of employees')
    phone_id: int = Field(default=0, alias='phone_id', description='Phone ID')
    token_openai: str = Field(default='', alias='token_openai', description='OpenAI token')
    plan: EmpresaPlan = Field(default=EmpresaPlan.BASIC, alias='plan', description='Company plan')
    status: ControlStatus = Field(default=ControlStatus.OKAY, alias='status', description='Company status')
