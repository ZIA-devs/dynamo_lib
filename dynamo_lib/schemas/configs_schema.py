from ..core.enums import EmpresaPlan, EmpresaTipo
from pydantic import BaseModel, Field, field_validator
from typing import Any, Dict
import json


class ConfigsSchema(BaseModel):
    assistant_id: str = Field(default='', alias='assistant_id', description='ID of the assistant')
    assistant_name: str = Field(default='', alias='assistant_name', description='Name of the assistant')
    business_type: EmpresaTipo = Field(default=EmpresaTipo.PADRAO, alias='business_type', description='Type of business')
    phone_id: str = Field(default='', alias='phone_id', description='ID of the phone')
    company_name: str = Field(default='', alias='company_name', description='Name of the company')
    employee_limit: int = Field(default=99, alias='employee_limit', description='Limit of employees')
    plan: EmpresaPlan = Field(default=EmpresaPlan.SCHEDULE, alias='plan', description='Plan of the company')
    token_google_calendar: Dict[str, Any] = Field(default_factory=dict, alias='token_google_calendar', description='Google Calendar token')
    token_asa: str = Field(default='', alias='token_asa', description='ASA token')
    token_openai: str = Field(default='', alias='token_openai', description='OpenAI token')
    token_wpp: str = Field(default='', alias='token_wpp', description='WhatsApp token')
    waba_id: str = Field(default='', alias='waba_id', description='WhatsApp Business Account ID')

    @field_validator('phone_id', mode='before')
    @classmethod
    def convert_phone_id_to_str(cls, v: int|str) -> str: return str(v)


    @field_validator('token_google_calendar', mode='before')
    @classmethod
    def convert_token_google_calendar_to_dict(cls, v: str|Dict[str, Any]) -> Dict[str, Any]: 
        return json.loads(v) if isinstance(v, str) else v
